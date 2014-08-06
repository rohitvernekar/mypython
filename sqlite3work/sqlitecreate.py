#!/usr/bin/python

import sqlite3 as lite
import sys

con = lite.connect('test.db')

with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE Cars(Id INT,Name TEXT,Price INT)")
    cur.execute("INSERT INTO Cars VALUES(1,'Audi',56778889)")
    cur.execute("INSERT INTO Cars VALUES(2,'Mercidez',36778889)")
    cur.execute("INSERT INTO Cars VALUES(3,'Skoda',343242227)")
    cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29470921)")
    cur.execute("INSERT INTO Cars VALUES(5,'Hummer',812347)")
    cur.execute("INSERT INTO Cars VALUES(6,'Maruti',1118889)")
