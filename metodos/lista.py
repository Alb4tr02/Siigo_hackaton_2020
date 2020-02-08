#!/usr/bin/python3

import MySQLdb

def listar():
       db = MySQLdb.connect(host="localhost", user="root",passwd="k@m1l0her196", db="prueba")
       cursor = db.cursor()
       table = cursor.execute("SELECT * FROM second_table")

       for row in range(table):
              print (cursor.fetchone())
       db.close()
