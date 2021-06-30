import sqlite3
import sql

db_name = 'optics_database'

# ---------TABLE CREATION-----------------
def connect():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(sql.table_creation)
    conn.commit()
    conn.close()

# ---------TABLE CREATION END-----------------

# ---------INSERTION-----------------
def insert_stu(name,reg,rol,course,sem,sex):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(sql.student_info,(name,reg,rol,course,sem,sex))
    conn.commit()
    conn.close()

#-------------------SHOWING ALL DATA OF THE RSPECTIVE TABLE---------------------
def show_stu():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(sql.view_all_stds)
    stus = c.fetchall() #this will grab all the records and return them as a tuple
    conn.commit()
    conn.close()
    return stus

#------------------------------------------------------
def show_sems(s):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT * FROM "+ str(s))
    semss=c.fetchall()
    conn.commit()
    conn.close() 
    return semss


def find_stu(name='',reg='',roll='',course='',sem='',sex=''):
    conn=sqlite3.connect(db_name)
    c=conn.cursor()
    c.execute(""" SELECT * FROM students WHERE
    name=? OR regno=? OR roll=? OR course=? OR sem=? OR sex=?
    
    """,(name,reg,roll,course,sem,sex))
    row = c.fetchall()
    conn.commit()
    conn.close()
    return row
#------------------------------------------------------

def de_l(reg,table_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("DELETE FROM "+ table_name +" WHERE regno=(?)" ,(reg,))
    conn.commit()
    conn.close()
#------------------------------------------------------

def upadate_stu(name,reg,roll,course,sem,sex):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(sql.upd_stu,(name,roll,course,sem,sex,reg))
    conn.commit()
    conn.close()

def check():
    if len(show_stu())==0:
        return False
    else:
        return True

def insert_sem(*args):
    pass

connect()