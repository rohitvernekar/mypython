#!/usr/bin/python


import sqlite3 as lite
import sys

con=lite.connect('test.db')
con.row_factory = lite.Row
print dir(con.row_factory)
with con:
    cur=con.cursor()
    cur.execute("select * from cars")
    rows = cur.fetchone()
    print rows     
