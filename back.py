import sqlite3

db_name=''

def connect():
    conn= sqlite3.connect(db_name)
    c=conn.cursor()
    c.execute("""
           
    """)
    conn.commit()
    conn.close()