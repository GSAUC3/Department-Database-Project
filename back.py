import sqlite3
import sql

db_name = 'optics_database'

# ---------TABLE CREATION-----------------
def connect(seql):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(seql)
    conn.commit()
    conn.close()

# ---------TABLE CREATION END-----------------

# ---------INSERTION-----------------
def insert_stu(name,reg,rol,course,sem,sex):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("INSERT INTO students (name,regno,roll,course,sem,sex) VALUES(?,?,?,?,?,?)"
    ,(name,reg,rol,course,sem,sex))
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


def insert_sem(*args):
    pass


def drop_table(tab):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("DROP TABLE "+tab)
    conn.commit()
    conn.close()
    pass
# connect(sql.table_stu)
def check():
    if len(show_stu())==0:
        return False
    else:
        return True

connect(sql.table_stu)       
connect(sql.tsm1)
connect(sql.tsm2)
connect(sql.tsm3)
connect(sql.tsm4)
connect(sql.tsm5)
connect(sql.tsm6)
connect(sql.tsm7)
connect(sql.tsm8)
#------------------------------------------------------------------
def login():
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    c.execute(sql.logg)
    conn.commit()
    conn.close()

def sign(user,pas):
    
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    c.execute("Insert INTO admin (userid,password) values(?,?)",(user,pas))
    conn.commit()
    conn.close()

def in_log(user,pas):
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    c.execute("SELECT * FROM admin WHERE userid=?",(user,))
    # c.execute("SELECT * FROM admin WHERE userid='" + user + "'")
    
    amni=c.fetchall()
    conn.commit()
    # print (str(amni[0][1]))
    conn.close()
    if amni[0][1]==pas:
        return True
    else:
        return False

login()

