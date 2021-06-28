import sqlite3
import sql

db_name = ''

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
def show_only_stu():
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

#------------------------------------------------------

def de_l(reg,table_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("DELETE FROM "+ table_name +" WHERE regno=(?)" ,(reg,))
    conn.commit()
    conn.close()
#------------------------------------------------------

def upadate():
    pass

