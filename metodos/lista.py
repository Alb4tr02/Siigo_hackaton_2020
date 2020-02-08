#!/usr/bin/env python3

import MySQLdb


def list_table_id(table="*", id=""):
       params = ["id", "tenant_id", "name", "description", "list_price"]
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
              total = {}
              for row in range(table):
                     response = {}
                     i = 0
                     aux = list(cursor.fetchone())
                     for value in aux:
                            response[params[i]] = aux[i]
                            i = i +  1
                     total[aux[0]] = response
              return total
