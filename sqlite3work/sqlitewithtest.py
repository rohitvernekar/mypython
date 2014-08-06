#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con=None


con=lite.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute('select sqlite_version()')
    data = cur.fetchone()
    print "SQLite version: %s" %data

   
