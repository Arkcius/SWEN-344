from src.swen344_db_utils import *
import csv

#creates tables
def rebuildTables():
    conn = connect()
    cur = conn.cursor()
    #drops tables
    drop_sql = """
        DROP TABLE IF EXISTS checkedout;
        DROP TABLE IF EXISTS libraryinventory;
        DROP TABLE IF EXISTS users;
        DROP TABLE IF EXISTS inventory;
        DROP TABLE IF EXISTS btype;
        DROP TABLE IF EXISTS library; 
    """
    #makes user table
    users_sql = """
        CREATE TABLE users(
            userID serial primary key,
            username varchar(50),
            contact varchar(50),
            active boolean default cast(1 as boolean)
        )
    """
    #makes type table
    type_sql = """
        CREATE TABLE btype(
            ID serial primary key,
            types varchar(50)
        )
    """
    #makes inventory table
    inventory_sql = """
        CREATE TABLE inventory(
            bookID serial primary key,
            title varchar(100),
            author varchar(100),
            publish char(10),
            copies int,
            type int not null,
            subtype int,
            comments varchar(128),
            FOREIGN KEY (type) REFERENCES BTYPE(ID)
        )
    """
    #makes checkout table
    checkedout_sql = """
        CREATE TABLE checkedout(
            IDuser int not null,
            IDbook int not null,
            outday date not null,
            returnday DATE,
            reserve boolean default cast(0 as boolean),
            overdueday date,
            overdue boolean default cast(0 as boolean),
            fee float,
            FOREIGN KEY (IDuser) REFERENCES USERS(userID),
            FOREIGN KEY (IDbook) REFERENCES INVENTORY(bookID)
        )
    """
    library_sql = """
        CREATE TABLE checkedout(
            libID serial primary key,
            libName varchar(50)
        )
    """
    libraryInventory_sql = """
        CREATE TABLE checkedout(
            IDlib int not null,
            IDbooks int not null,
            localcopies int,
            FOREIGN KEY (IDlib) REFERENCES LIBRARY(libID),
            FOREIGN KEY (IDbooks) REFERENCES INVENTORY(bookID)
        )
    """
    #executes all sql and closes
    cur.execute(drop_sql)
    cur.execute(users_sql)
    cur.execute(type_sql)
    cur.execute(inventory_sql)
    cur.execute(checkedout_sql)
    conn.commit()
    conn.close()

def loadFile(path):
    full_path = os.path.join(os.path.dirname(__file__), f'../../{path}')
    with open(full_path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        for row in reader:
                type1 = getTypeName(row[3])
                type2 = getTypeName(row[4])
                if type2 == "None":
                    makeNewType(row[4])
                    type2 = getTypeName(row[4])
                for i in range(0,3):
                    row[i] = row[i].replace("\'","\'\'")
                add = """
                INSERT INTO inventory(title,author,comments,type,subtype,copies)
                VALUES('"""+str(row[0])+"""', '"""+str(row[1])+"""', '"""+str(row[2])+"""'
                , '"""+str(type1)+"""', '"""+str(type2)+"""', '"""+str(row[5])+"""')
                """
                exec_commit(add)

def getTypeName(types):
    result = exec_get_one("SELECT btype.ID FROM btype WHERE types = '"+types+"'")
    if result == None:
        return "None"
    return result[0]

def makeNewType(types):
    exec_commit("INSERT INTO btype(types) VALUES('"+types+"')")
    
#gets all users
def getUsers():
    result = exec_get_all("SELECT * FROM users")
    return result

#gets specific user when given username
def getUser(username):
    result = exec_get_all("SELECT * FROM users WHERE username = '" + username +"'")
    return result

#gets all books and their info from inventory
def getBooks():
    result = exec_get_all("SELECT * FROM inventory")
    return result

#gets book infor from title
def getBooktitle(title):
    result = exec_get_all("SELECT * FROM inventory WHERE title = '" + title +"'")
    return result

#gets all books of specific type
def getBookType(type):
    result = exec_get_all("SELECT inventory.title,inventory.copies FROM inventory WHERE type = "+str(type))
    return result

#gets all types
def getTypes():
    result = exec_get_all("SELECT * FROM btype")
    return result

#gets users checked out books from their username
def getUserCheckout(username):
    checkout = """
        SELECT users.username, inventory.title, checkedout.outday, checkedout.returnday FROM checkedout 
            INNER JOIN users ON checkedout.IDuser = users.userID
            INNER JOIN inventory ON checkedout.IDbook = inventory.bookID
            WHERE users.username = '"""+str(username) + """'
            ORDER BY inventory.title
            """
    result = exec_get_all(checkout)
    return result

#gets all user checkouts
def getUserCheckouts():
    checkout = """
        SELECT users.username, inventory.title FROM checkedout 
            INNER JOIN users ON checkedout.IDuser = users.userID
            INNER JOIN inventory ON checkedout.IDbook = inventory.bookID
            ORDER BY users.username
            """
    result = exec_get_all(checkout)
    return result

def getBookCheckouts():
    checkout = """
        SELECT users.username, inventory.title, checkedout.outday, checkedout.returnday, inventory.copies FROM checkedout 
            INNER JOIN users ON checkedout.IDuser = users.userID
            INNER JOIN inventory ON checkedout.IDbook = inventory.bookID
            ORDER BY inventory.type, inventory.author
            """
    result = exec_get_all(checkout)
    return result
def addUser(username,contact):
    add = """
        INSERT INTO users(username, contact)
            VALUES('"""+str(username)+"""', '"""+str(contact)+"""')
        """
    exec_commit(add)

def deactivateUser(username):
    delete = """
        UPDATE users SET active=FALSE 
        WHERE username = '"""+str(username)+"""'
        """
    exec_commit(delete)

def getUserID(username):
    result = exec_get_one("SELECT users.userID FROM users WHERE username = '"+str(username)+"'")
    return result[0]
def getBookID(title):
    result = exec_get_one("SELECT inventory.bookID FROM inventory WHERE title = '" + title +"'")
    return result[0]
def getLibraryID(library):
    result = exec_get_one("SELECT library.libID FROM library WHERE libName = '"+str(library)+"'")
    return result[0]

def getBooksCopies(title):
    result = exec_get_one("SELECT inventory.copies FROM inventory WHERE title = '" + title +"'")
    return result[0]

def getUserReserve(username):
    reserve = """
        SELECT users.username, inventory.title, checkedout.reserve FROM checkedout 
            INNER JOIN users ON checkedout.IDuser = users.userID
            INNER JOIN inventory ON checkedout.IDbook = inventory.bookID
            WHERE users.username = '"""+str(username) + """' AND reserve = TRUE
            ORDER BY inventory.title
    """
    result = exec_get_all(reserve)
    return result

def checkout(username,title,library,date):
    if len(checkLateUser(username))>0:
        return None
    elif getLocalCopies(title,library)>0:
        checkout = """
            INSERT INTO checkedout(IDuser,IDbook,IDlib,outday,overdueday)
            VALUES('"""+str(getUserID(username))+"""', '"""+str(getBookID(title))+"""', '"""+str(getLibraryID(library))+"""','"""+str(date)+"""','"""+str(date)+"""+14')
        """
        exec_commit(checkout)
        update = """
            UPDATE inventory SET copies= copies-1 WHERE bookID = """+str(getBookID(title))+"""
        """
        exec_commit(update)
        update2 = """
            UPDATE libraryinventory SET localcopies= localcopies-1 WHERE IDbooks = """+str(getBookID(title))+"""
        """
        exec_commit(update2)
    else:
        checkout = """
            INSERT INTO checkedout(IDuser,IDbook,IDlib,outday,reserve)
            VALUES('"""+str(getUserID(username))+"""', '"""+str(getBookID(title))+"""', '"""+str(getLibraryID(library))+"""','"""+str(date)+"""','"""+str(1)+"""')
        """
        exec_commit(checkout)

def checkLateUser(username):
    overdue = """
        SELECT users.username, inventory.title, checkedout.overdue FROM checkedout 
            INNER JOIN users ON checkedout.IDuser = users.userID
            INNER JOIN inventory ON checkedout.IDbook = inventory.bookID
            WHERE users.username = '"""+str(username) + """' AND overdue = TRUE
            ORDER BY inventory.title
    """
    result = exec_get_all(overdue)
    return result

def checkLateUsers():
    overdue = """
        SELECT users.username, inventory.title, checkedout.overdue FROM checkedout 
            INNER JOIN users ON checkedout.IDuser = users.userID
            INNER JOIN inventory ON checkedout.IDbook = inventory.bookID
            WHERE overdue = TRUE
            ORDER BY users.username
    """
    result = exec_get_all(overdue)
    return result

def addBook(title,author,publish,copies,type):
    add = """
        INSERT INTO inventory(title,author,publish,copies,type)
            VALUES('"""+str(title)+"""', '"""+str(author)+"""', '"""+str(publish)+"""'
            , '"""+str(copies)+"""', '"""+str(type)+"""')
        """
    exec_commit(add)

#returns book based on user title and date and then sets overdue back to false
def returnBook(username,title,date):
    if getBooksCopies(title)>0:
        returnal = """
            UPDATE checkedout SET returnday = '"""+str(date)+"""' WHERE IDbook = """+str(getBookID(title))+""" AND IDuser ='"""+str(getUserID(username))+"""'
            """
        returnal2 = """
            UPDATE checkedout SET overdue = '0' WHERE IDbook = """+str(getBookID(title))+""" AND IDuser ='"""+str(getUserID(username))+"""'
            """ 
        exec_commit(returnal)
        exec_commit(returnal2)
        update = """
            UPDATE inventory SET copies= copies+1 WHERE bookID = """+str(getBookID(title))+"""
        """
        exec_commit(update)
        update2 = """
            UPDATE libraryinventory SET localcopies= localcopies+1 WHERE IDbooks = """+str(getBookID(title))+"""
        """
        exec_commit(update2)
        days,fee = LateFee(username,title)
        return days,fee

def getLocalCopies(title,library):
    cop = """
        SELECT libraryinventory.localcopies FROM libraryinventory
        WHERE IDlib = '"""+str(getLibraryID(library))+"""' AND IDbooks = '"""+str(getBookID(title))+"""'
    """
    result = exec_get_one(cop)
    return result[0]

def getUserHistory(username):
    overdue = """
        SELECT users.username, inventory.title FROM checkedout 
            INNER JOIN users ON checkedout.IDuser = users.userID
            INNER JOIN inventory ON checkedout.IDbook = inventory.bookID
            WHERE users.username = '"""+str(username) + """' AND overdue = TRUE
            ORDER BY checkedout.outday
    """
    result = exec_get_all(overdue)
    return result
    

def addCopiesToLibrary(library,title,copies):
    bid = getBookID(title)
    lid = getLibraryID(library)
    adder = """
        INSERT INTO libraryinventory(IDlib,IDbooks,localcopies) VALUES ('"""+str(lid)+"""','"""+str(bid)+"""','"""+str(copies)+"""')
    """
    exec_commit(adder)

def makeOverdue(username,title):
    overdue = """
            UPDATE checkedout SET overdue = '1' WHERE IDbook = """+str(getBookID(title))+""" AND IDuser ='"""+str(getUserID(username))+"""'
            """ 
    exec_commit(overdue)

def getAllLocal():
    allLib = """
            SELECT library.libName, inventory.title, libraryinventory.localcopies FROM libraryinventory 
                INNER JOIN library ON libraryinventory.IDlib = library.libID
                INNER JOIN inventory ON libraryinventory.IDbooks = inventory.bookID
                ORDER BY library.libName, inventory.title
        """
    result = exec_get_all(allLib)
    return result

def LateFee(username,title):

    getDates = """ 
        SELECT returnday,overdueday FROM CHECKEDOUT WHERE IDbook = """+str(getBookID(title))+""" AND IDuser ='"""+str(getUserID(username))+"""'
    """
    result = exec_get_one(getDates)
    
    day = result[0]-result[1]
    days = day.days
    daysret = days
    fee=0.0
    if days > 0:
        fee = 0.25
        if days>7:
            days-=7
            while days>0:
                fee += 2.00
                days-=1
    
    updateFee = """
        UPDATE checkedout SET fee = """+str(fee)+""" WHERE IDbook = """+str(getBookID(title))+""" AND IDuser ='"""+str(getUserID(username))+"""'
    """
    exec_commit(updateFee)
    return daysret,fee


def BookTable():
    getBooks = """
        SELECT string_agg(inventory.title,inventory.author) AS titler, users.username FROM checkedout 
            INNER JOIN users ON checkedout.IDuser = users.userID
            INNER JOIN inventory ON checkedout.IDbook = inventory.bookID
            GROUP BY title, author
    """
    return exec_get_all(getBooks)

def getUserInfo():
    getUserInfo = """
        SELECT user.username, inventory.title, checkedout.overdueday, checkedout.fee FROM CHECKEDOUT
            INNER JOIN users ON checkedout.IDuser = users.userID
            INNER JOIN inventory ON checkedout.IDbook = inventory.bookID
            ORDER BY checkedout.IDlib, checkedout.IDuser,checkedout.IDbook,checkedout.overdueday
    """
    return exec_get_all(getUserInfo)