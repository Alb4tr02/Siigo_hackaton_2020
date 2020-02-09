#!/usr/bin/env python3

import MySQLdb


def get_params(table_name):
       db = MySQLdb.connect(host="localhost", user="electros", passwd="electros", db="siigo")
       cursor = db.cursor()
       table = cursor.execute("SHOW COLUMNS FROM " + table_name)
       params = []
       for row in range(table):
              aux = list(cursor.fetchone())
              params.append(str(aux[0]))
       return params

def list_all_table(table_name):
       db = MySQLdb.connect(host="localhost", user="electros", passwd="electros", db="siigo")
       cursor = db.cursor()
       query = "SELECT * FROM " + table_name
       total = {}
       params = get_params(table_name)
       table = cursor.execute(query)
       for row in range(table):
              response = {}
              i = 0
              aux = list(cursor.fetchone())
              for value in aux:
                     response[params[i]] = aux[i]
                     i = i +  1
                     total[aux[0]] = response
       return total

def list_table_id(table_name, id):
       try:
              params = get_params(table_name)
              db = MySQLdb.connect(host="localhost", user="electros", passwd="electros", db="siigo")
              cursor = db.cursor()
              query = "SELECT * FROM " + table_name + " WHERE id = " + id
              table = cursor.execute(query)
              response = {}
              aux = list(cursor.fetchone())
              i = 0
              for value in aux:
                     response[params[i]] = aux[i]
                     i = i +  1
              return response
       except:
              return {'error': 'Can not show this id {} on the table {} because it does not exist'.format(id, table_name)}
