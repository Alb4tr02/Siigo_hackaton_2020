#!/usr/bin/env python3

import MySQLdb


def insert_into_table(table_name, data):
    db = MySQLdb.connect(host="localhost", user="electros", passwd="electros", db="siigo")
    cursor = db.cursor()
    query = "INSERT INTO " + table_name + "("
    values = "VALUES ("
    sep = ""
    for key, value in data.items():
        query = query + sep + key
        values = values + sep + "'" + value + "'"
        sep = ", "
    query = query + ") " + values + ") "
    cursor.execute(query)
    db.commit()
    db.close()
