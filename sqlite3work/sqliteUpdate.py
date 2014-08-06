#!/usr/bin/python
import sqlite3 as lite
import sys
uid=1
uname="Honda"

con=lite.connect('test.db')

with con:
    cur=con.cursor()
    cur.execute("Update Cars SET Name = ? where Id=?",(uname,uid))
    con.commit()
    
    print "Number of rows updated: %d" % cur.rowcount 
