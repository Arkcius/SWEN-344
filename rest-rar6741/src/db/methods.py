import os
import hashlib
import secrets
from .swen344_db_utils import *

def rebuild_tables():
    exec_sql_file('src/db/schema.sql')
    exec_sql_file('src/db/test_data.sql')

def list_examples():
    """This is an example. Please remove from your code before REST1 deadline.
    DB layer call for listing all rows of our example.
    """
    return exec_get_all('SELECT id, foo FROM example_table')

def list_users():
    return exec_get_all('SELECT * FROM users')

def list_books(genre,author,title):
    ex = 'SELECT books.id,books.title,books.author,btype.genre FROM books INNER JOIN btype ON books.genre = btype.id'
    count = 0
    if genre!=None:
        ex = ex+' WHERE btype.genre = \''+genre+'\''
        count+=1
    if author!=None:
        if count > 0:
            ex = ex + ' AND author = \''+author+'\''
        else:
            ex = ex+' WHERE author = \''+author+'\''
        count+=1
    if title!=None:
        if count > 0:
            ex = ex + ' AND title = \''+title+'\''
        else:
            ex = ex+' WHERE title = \''+title+'\''
        count+=1
    return exec_get_all(ex)

def list_books_genre(genre):
    return exec_get_all('SELECT * FROM books WHERE genre = '+genre)

def addUser(firstname,lastname,contact,password):
    pas = hashlib.sha512()
    pas.update(password.encode('utf-8'))
    ret = exec_get_all('SELECT * FROM users WHERE firstname = \''+firstname+'\' AND lastname = \''+lastname+'\'')
    if(len(ret)<=0):
        vals = "('"+firstname+"', '"+lastname+"', '"+contact+"', '"+str(pas.hexdigest())+"')"
        exec_commit('INSERT INTO users(firstname,lastname,contact,password) VALUES'+vals)
        return True
    else:
        return False

def deleteUser(firstname,lastname,session):
    ret = exec_get_one('SELECT id FROM users WHERE firstname = \''+firstname+'\' AND lastname = \''+lastname+'\' AND sessionKey = \''+str(session)+'\'')
    if(ret!=None):
        exec_commit('DELETE FROM users WHERE id = '+str(ret[0]) )
        return True
    else:
        return False
    

def updateUser(id,firstname,lastname,contact,password):
    ret = exec_get_all('SELECT * FROM users WHERE id =' +str(id))
    pas = hashlib.sha512()
    pas.update(password.encode('utf-8'))
    if(len(ret)==1):
        exec_commit('UPDATE users SET firstname = \''+firstname+'\', lastname = \''+lastname+'\', contact = \''+contact+'\', password = \''+str(pas.hexdigest())+'\' WHERE id = '+str(id))
        return True
    else:
        return False
    
def loginUser(firstname, password):
    pas = hashlib.sha512()
    pas.update(password.encode('utf-8'))
    session = secrets.token_hex(16)
    id = exec_get_one('SELECT id FROM users WHERE firstname = \''+firstname+'\' AND password = \''+str(pas.hexdigest())+'\'')
    ret = exec_get_all('SELECT * FROM users WHERE id = '+str(id[0]))
    if(len(ret)==1):
        exec_commit('UPDATE users SET sessionKey = \''+str(session)+'\' WHERE id = '+str(id[0]))
        print("update")
        return session
    else:
        return ""
    
def getCheckouts():
    ret = exec_get_all('SELECT * FROM checkouts')
    return ret

def Checkout(title,session,reserve):
    userid = exec_get_all('SELECT id FROM users WHERE sessionKey = \''+session+'\'')
    bookid = exec_get_all('SELECT id FROM books WHERE title = \''+title+'\'')
    if(len(userid)==1&len(bookid)==1):
        if(reserve==False):
            exec_commit('INSERT INTO checkouts(bookID,userID) VALUES(\''+str(bookid[0][0])+'\', \''+str(userid[0][0])+'\')')
        elif(reserve == True):
            exec_commit('INSERT INTO checkouts(bookID,userID,reserve) VALUES(\''+str(bookid[0][0])+'\', \''+str(userid[0][0])+'\', \''+str(1)+'\')')
        return True
    else:
        return False
    
    
