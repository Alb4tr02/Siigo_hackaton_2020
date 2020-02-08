#!/usr/bin/env python3

import MySQLdb


def list_table_id(table="*", id=""):
       db = MySQLdb.connect(host="localhost", user="electros", passwd="electros", db="siigo")
       cursor = db.cursor()
       query = "SELECT * FROM " + table
       if (table == "*"):
              query = "SELECT TABLE_NAME FROM  INFORMATION_SCHEMA.tables WHERE TABLE_SCHEMA='siigo';"
              table = cursor.execute(query)
              tables = []
              for row in range(table):
                     table_name = list(cursor.fetchone())
                     tables.append(str(table_name[0]))
              for name in tables:
                     list_table_id(name, "")
       else:
              if (len(id) != 0):
                     query = "SELECT * FROM " + table + " WHERE id = " + id
              table = cursor.execute(query)
              for row in range(table):
                     print (cursor.fetchone())
