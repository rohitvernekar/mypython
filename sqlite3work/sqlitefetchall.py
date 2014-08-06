#!/usr/bin/python
import sqlite3 as lite
import sys

con=lite.connect('test.db')
with con:
    cur=con.cursor()
    cur.execute("select * from Cars")
    
    rows=cur.fetchall()
    print rows
    for row in rows:
        print row
