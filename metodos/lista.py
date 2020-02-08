#!/usr/bin/python3

import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="electros", db="siigo")
cursor = db.cursor()

def list_ac_invoice_items():
       table = cursor.execute("SELECT * FROM ac_invoice_items")
       for row in range(table):
              print (cursor.fetchone())

def list_ac_invoices():
       table = cursor.execute("SELECT * FROM ac_invoices")
       for row in range(table):
              print (cursor.fetchone())

def list_ac_products():
       table = cursor.execute("SELECT * FROM ac_products")
       for row in range(table):
              print (cursor.fetchone())

def list_ac_tenant():
       table = cursor.execute("SELECT * FROM ac_tenant")
       for row in range(table):
              print (cursor.fetchone())

def list_customer():
       table = cursor.execute("SELECT * FROM customer")
       for row in range(table):
              print (cursor.fetchone())

def list_all():
       print("Table : ac_invoice_items")
       list_ac_invoice_items()
       print("Table : ac_invoice")
       list_ac_invoices()
       print("Table : ac_products")
       list_ac_products()
       print("Table : ac_tenant")
       list_ac_tenant()
       print("Table : customer")
       list_customer()
