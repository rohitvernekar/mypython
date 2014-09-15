#!/usr/bin/python


import sqlite3 as lite
import sys
import pdb;pdb.set_trace()
con=lite.connect('test.db')
con.row_factory = lite.Row
#print dir(con.row_factory)
with con:
    cur=con.cursor()
    cur.execute("select Name from cars where id=1")
    rows = cur.fetchone()

    print rows[0]     
