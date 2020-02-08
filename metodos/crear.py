#!/usr/bin/python

import MySQLdb

def crear():
    db = MySQLdb.connect(host="localhost", user="root",passwd="k@m1l0her196", db="prueba")
    cursor = db.cursor()

    command = "INSERT INTO second_table(ID, NAME, SCORE) VALUES ('6', 'Jimmer', 17);"
    cursor.execute(command)
    db.commit()
    db.close()
