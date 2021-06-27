import sqlite3

db_name = ''

# ---------TABLE CREATION-----------------
def connect():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("""CREATE TABLE students IF NOT EXISTS (
        name text NUT NULL,
        regno text NOT NULL PRIMARY KEY,
        roll text NOT NULL,
        course VARCHAR(6) NOT NULL,
        sem VARCHAR(3) NOT NULL,
        sex VARCHAR(7)
        );
            CREATE TABLE sem7 IF NOT EXISTS (
        regno text NOT NULL PRIMARY KEY,
        B471 REAL NOT NULL,
        B472 REAL NOT NULL,
        B473 REAL NOT NULL,
        B474 REAL NOT NULL,
        B475 REAL NOT NULL,
        B471D REAL NOT NULL,
        B471P REAL NOT NULL,
        B472P REAL NOT NULL,
        B473P REAL NOT NULL,
        cgpa REAL NOT NULL,
        passed Boolean NOT NULL
        );

        CREATE TABLE sem6 IF NOT EXISTS (
        regno text NOT NULL PRIMARY KEY,
        B461 REAL NOT NULL,
        B462 REAL NOT NULL,
        B463 REAL NOT NULL,
        B464 REAL NOT NULL,
        B465 REAL NOT NULL,
        B361P REAL NOT NULL,
        B362P REAL NOT NULL,
        B363P REAL NOT NULL,
        B364P REAL NOT NULL,
        cgpa REAL NOT NULL,
        passed Boolean NOT NULL
        );

        CREATE TABLE sem5 IF NOT EXISTS (
        regno text NOT NULL PRIMARY KEY,
        B451 REAL NOT NULL,
        B452 REAL NOT NULL,
        B453 REAL NOT NULL,
        B454 REAL NOT NULL,
        B455 REAL NOT NULL,
        B351P REAL NOT NULL,
        B352P REAL NOT NULL,
        B351S REAL NOT NULL,
        cgpa REAL NOT NULL,
        passed Boolean NOT NULL
        );

        CREATE TABLE sem4 IF NOT EXISTS (
        regno text NOT NULL PRIMARY KEY,
        B241 REAL NOT NULL,
        B242 REAL NOT NULL,
        B243 REAL NOT NULL,
        B244 REAL NOT NULL,
        B245 REAL NOT NULL,
        B246 REAL NOT NULL,
        B241P REAL NOT NULL,
        B242P REAL NOT NULL,
        cgpa REAL NOT NULL,
        passed Boolean NOT NULL
        );


        CREATE TABLE sem8 IF NOT EXISTS (
        regno text NOT NULL PRIMARY KEY,
        B481S REAL NOT NULL,
        B482D REAL NOT NULL,
        B483V REAL NOT NULL,
        cgpa REAL NOT NULL,
        passed Boolean NOT NULL
        );

        CREATE TABLE sem1 IF NOT EXISTS (
        regno text NOT NULL PRIMARY KEY,
        HU101 REAL NOT NULL,
        PH102 REAL NOT NULL,
        CH103 REAL NOT NULL,
        MA104 REAL NOT NULL,
        EE105 REAL NOT NULL,
        CS106 REAL NOT NULL,
        HU107 REAL NOT NULL,
        PH108 REAL NOT NULL,
        CH109 REAL NOT NULL,
        EE110 REAL NOT NULL,
        CS111 REAL NOT NULL,
        cgpa REAL NOT NULL,
        passed Boolean NOT NULL
        );

        CREATE TABLE sem2 IF NOT EXISTS (
        regno text NOT NULL PRIMARY KEY,
        HU201 REAL NOT NULL,
        PH202 REAL NOT NULL,
        CH203 REAL NOT NULL,
        MA204 REAL NOT NULL,
        ET205 REAL NOT NULL,
        ME206 REAL NOT NULL,
        PH207 REAL NOT NULL,
        CH208 REAL NOT NULL,
        ET209 REAL NOT NULL,
        ME210 REAL NOT NULL,
        ME211 REAL NOT NULL,
        cgpa REAL NOT NULL,
        passed Boolean NOT NULL
        );

        CREATE TABLE sem3 IF NOT EXISTS (
        regno text NOT NULL PRIMARY KEY,
        B231 REAL NOT NULL,
        B232 REAL NOT NULL,
        B233 REAL NOT NULL,
        B234 REAL NOT NULL,
        B235 REAL NOT NULL,
        B231P REAL NOT NULL,
        B232P REAL NOT NULL,
        cgpa REAL NOT NULL,
        passed Boolean NOT NULL
        );
        """)
    conn.commit()
    conn.close()

# ---------TABLE CREATION END-----------------

# ---------INSERTION-----------------
def insert_stu(name,reg,rol,course,sem,sex):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("""
    INSERT INTO students VALUES(?,?,?,?,?,?),
    """,(name,reg,rol,course,sem,sex)
    )
    conn.commit()
    conn.close()
#------------------------------------------------------

#-------------------SHOWING ALL DATA OF THE RSPECTIVE TABLE---------------------
def show_only_stu():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("""
    SELECT * FROM students
    """)
    stus = c.fetchall() #this will grab all the records and return them as a tuple
    conn.commit()
    conn.close()
    return stus

def show_sem1():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("""
    
    """)
    conn.commit()
    conn.close() 

def show_sem2():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("""
    
    """)
    conn.commit()
    conn.close()

def show_sem3():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("""
    
    """)
    conn.commit()
    conn.close()

def show_sem4():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("""
    
    """)
    conn.commit()
    conn.close()

def show_sem5():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("""
    
    """)
    conn.commit()
    conn.close()

def show_sem6():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("""
    
    """)
    conn.commit()
    conn.close()

def show_sem7():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("""
    
    """)
    conn.commit()
    conn.close()

def show_sem8():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("""
    
    """)
    conn.commit()
    conn.close()
#------------------------------------------------------