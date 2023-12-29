from src.swen344_db_utils import *




def rebuildTables():
    exec_sql_file('./univ_finance.sql')


def printResults(Result,Col,Q):
    print("Question-"+str(Q))
    x=0
    while x < len(Result):
        i = 0
        printer = ""
        while i < Col:
            printer = printer + str(Result[x][i])+", "
            i+=1
        print(printer)
        x+=1

def question1():
    Report = """
        SELECT dept.name, faculty.last_name, faculty.first_name, position.title, salaries.salary, faculty.hire_date, contracts.start_date, contracts.end_date FROM FACULTY
        INNER JOIN dept on faculty.dept_id = dept.id
        INNER JOIN position on faculty.position_id = position.id
        INNER JOIN salaries on faculty.id = salaries.faculty_id
        INNER JOIN contracts on faculty.id = contracts.faculty_id
        ORDER BY dept.name, faculty.hire_date 
    """
    result = exec_get_all(Report)
    return result

def getDept(dept):
    result = exec_get_one("SELECT dept.ID FROM dept where name = '"+str(dept)+"'")
    return result[0]

def getPosition(position):
    result = exec_get_one("SELECT position.ID FROM position where title = '"+str(position)+"'")
    return result[0]

def getFaculty(firstname,lastname):
    result = exec_get_one("SELECT faculty.id FROM faculty where first_name = '"+str(firstname)+"' AND last_name = '"+str(lastname)+"'")
    return result[0]

def addNew(firstname, lastname, dept,position, hiredate, salary):
    deptnum = getDept(dept)
    positionnum = getPosition(position)

    faculty = """
        INSERT INTO faculty(first_name,last_name,dept_id,position_id,hire_date)
        VALUES('"""+str(firstname)+"""','"""+str(lastname)+"""','"""+str(deptnum)+"""','"""+str(positionnum)+"""','"""+str(hiredate)+"""')
    """
    exec_commit(faculty)
    facultynum = getFaculty(firstname,lastname)
    salary = """
        INSERT INTO salaries(faculty_id,salary,effective_date)
        VALUES('"""+str(facultynum)+"""', '"""+str(salary)+"""', '"""+str(hiredate)+"""')
    """
    exec_commit(salary)

    contract = """
        INSERT INTO contracts(faculty_id,start_date)
        VALUES('"""+str(facultynum)+"""', '"""+str(hiredate)+"""')
    """
    exec_commit(contract)

def getContract(firstname,lastname):
    result = exec_get_one("SELECT contracts.id FROM contracts where faculty_id = '"+str(getFaculty(firstname,lastname))+"'")
    return result[0]

def ModifyContractEnd(firstname,lastname,enddate):
    conNum = getContract(firstname,lastname)
    update = "UPDATE contracts SET end_date = '"+str(enddate)+"' WHERE id = "+str(conNum)
    exec_commit(update)
    #print(exec_get_one("SELECT end_date FROM contracts where id=26"))

def GetContracts():
    contract = """
        SELECT faculty.first_name, faculty.last_name,contracts.type,contracts.start_date,contracts.end_date FROM contracts
        INNER JOIN faculty ON contracts.faculty_id = faculty.id
        ORDER BY contracts.start_date 
    """
    return exec_get_all(contract)
    
def getFacultyDate(year):
    Report = """
        SELECT dept.name, faculty.last_name, faculty.first_name, position.title, salaries.salary, faculty.hire_date, contracts.start_date, contracts.end_date FROM FACULTY
        INNER JOIN dept on faculty.dept_id = dept.id
        INNER JOIN position on faculty.position_id = position.id
        INNER JOIN salaries on faculty.id = salaries.faculty_id
        INNER JOIN contracts on faculty.id = contracts.faculty_id
        WHERE faculty.hire_date > '"""+str(year)+"""-01-01'
        ORDER BY dept.name, faculty.hire_date 
        
    """
    result = exec_get_all(Report)
    return result