#!/usr/bin/env python3

import MySQLdb


def crear_ac_invoice_items(data):
    ID = data['id']
    TENANT_ID = data['tenant_id']
    PRODUCT_ID = data['product_id']
    INVOICE_ID = data['invoice_id']
    QUANTITY = data['quantity']
    UNIT_VALUE = data['unit_value']
    ITEM_VALUE = data['item_value']
    db = MySQLdb.connect(host="localhost", user="electros", passwd="electros", db="siigo")
    cursor = db.cursor()
    command = "INSERT INTO ac_invoice_items(ID, TENANT_ID, PRODUCT_ID, INVOICE_ID, QUANTITY, UNIT_VALUE, ITEM_VALUE) "
    values = "VALUES ({}, {}, {}, {}, {}, {}, {});".format(ID,
                                                           TENANT_ID,
                                                           PRODUCT_ID,
                                                           INVOICE_ID,
                                                           QUANTITY,
                                                           UNIT_VALUE,
                                                           ITEM_VALUE)
    command += values
    cursor.execute(command)
    db.commit()
    db.close()

def crear_ac_invoices(ID, TENANT_ID, CUSTOMER_ID, DOC_DATE, DOC_NUMBER, TOTAL_DISCOUNT, TOTAL_TAX, TOTAL_VALUE):
    db = MySQLdb.connect(host="localhost", user="electros", passwd="electros", db="siigo")
    cursor = db.cursor()
    command = "INSERT INTO ac_invoices(ID, TENANT_ID, CUSTOMER_ID, DOC_DATE, DOC_NUMBER, TOTAL_DISCOUNT, TOTAL_TAX, TOTAL_VALUE) "
    values = "VALUES ({}, {}, {}, '{}', '{}', {}, {}, {});".format(ID,
                                                               TENANT_ID,
                                                               CUSTOMER_ID,
                                                               DOC_DATE,
                                                               DOC_NUMBER,
                                                               TOTAL_DISCOUNT,
                                                               TOTAL_TAX,
                                                               TOTAL_VALUE)
    command += values
    cursor.execute(command)
    db.commit()
    db.close()



def crear_ac_products(data):
    ID = data['id']
    TENANT_ID = data['tenant_id']
    NAME = data['name']
    DESCRIPTION = data['description']
    LIST_PRICE = data['list_price']
    db = MySQLdb.connect(host="localhost", user="electros", passwd="electros", db="siigo")
    cursor = db.cursor()
    command = "INSERT INTO ac_products(ID, TENANT_ID, NAME, DESCRIPTION, LIST_PRICE) "
    values = "VALUES ({}, {}, '{}', '{}', {});".format(ID, TENANT_ID, NAME, DESCRIPTION, LIST_PRICE)
    command += values
    cursor.execute(command)
    db.commit()
    db.close()


def crear_ac_tenant(data):
    ID = data['id']
    NAME = data['name']
    db = MySQLdb.connect(host="localhost", user="electros", passwd="electros", db="siigo")
    cursor = db.cursor()
    command = "INSERT INTO ac_tenant(ID, NAME) "
    values = "VALUES ({}, '{}');".format(ID, NAME)
    command += values
    cursor.execute(command)
    db.commit()
    db.close()

def crear_customer(data):
    ID = data['id']
    TENANT_ID = data['tenant_id']
    FIRST_NAME = data['first_name']
    LAST_NAME = data['last_name']
    db = MySQLdb.connect(host="localhost", user="electros", passwd="electros", db="siigo")
    cursor = db.cursor()
    command = "INSERT INTO customer(ID, TENANT_ID, FIRST_NAME, LAST_NAME) "
    values = "VALUES ({}, {}, '{}', '{}');".format(ID, TENANT_ID, FIRST_NAME, LAST_NAME)
    command += values
    cursor.execute(command)
    db.commit()
    db.close()
