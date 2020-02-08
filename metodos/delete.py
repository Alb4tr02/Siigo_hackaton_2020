#!/usr/bin/env python3

import MySQLdb

db = MySQLdb.connect(host="localhost", user="electros", passwd="electros", db="siigo")
cursor = db.cursor()

def delete_row(ID, TABLE):
    command = "DELETE FROM {} WHERE id={}".format(TABLE, ID)
    cursor.execute(command)
    db.commit()
