#!/usr/bin/env python3

import MySQLdb


def crear_ac_invoice_items(ID, TENANT_ID, PRODUCT_ID, INVOICE_ID, QUANTITY, UNIT_VALUE, ITEM_VALUE):
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



def crear_ac_products(ID, TENANT_ID, NAME, DESCRIPTION, LIST_PRICE):
    db = MySQLdb.connect(host="localhost", user="electros", passwd="electros", db="siigo")
    cursor = db.cursor()
    command = "INSERT INTO ac_products(ID, TENANT_ID, NAME, DESCRIPTION, LIST_PRICE) "
    values = "VALUES ({}, {}, '{}', '{}', {});".format(ID, TENANT_ID, NAME, DESCRIPTION, LIST_PRICE)
    command += values
    cursor.execute(command)
    db.commit()
    db.close()


def crear_ac_tenant(ID, NAME):
    db = MySQLdb.connect(host="localhost", user="electros", passwd="electros", db="siigo")
    cursor = db.cursor()
    command = "INSERT INTO ac_tenant(ID, NAME) "
    values = "VALUES ({}, '{}');".format(ID, NAME)
    command += values
    cursor.execute(command)
    db.commit()
    db.close()

def crear_customer(ID, TENANT_ID, FIRST_NAME, LAST_NAME):
    db = MySQLdb.connect(host="localhost", user="electros", passwd="electros", db="siigo")
    cursor = db.cursor()
    command = "INSERT INTO customer(ID, TENANT_ID, FIRST_NAME, LAST_NAME) "
    values = "VALUES ({}, {}, '{}', '{}');".format(ID, TENANT_ID, FIRST_NAME, LAST_NAME)
    command += values
    cursor.execute(command)
    db.commit()
    db.close()
