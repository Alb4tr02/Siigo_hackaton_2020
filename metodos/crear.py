#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect(host="localhost", user="electros", passwd="electros", db="siigo")
cursor = db.cursor()

def crear_ac_invoice_items(ID, TENANT_ID, PRODUCT_ID, INVOICE_ID, QUANTITY, UNIT_VALUE, ITEM_VALUE):
    command = "INSERT INTO ac_invoice_items(ID, TENANT_ID, PRODUCT_ID, INVOICE_ID, QUANTITY, UNIT_VALUE, ITEM_VALUE) "
    values = "VALUES ({}, {}, {}, {}, {}, {}, {});".format(ID,
                                                           TENANT_ID,
                                                           PRODUCT_ID,
                                                           INVOICE_ID,
                                                           QUANTITY,
                                                           UNIT_VALUE,
                                                           ITEM_VALUE)
    cursor.execute(command + values)
    db.commit()

def crear_ac_invoices(ID, TENANT_ID, CUSTOMER_ID, DOC_DATE, DOC_NUMBER, TOTAL_DISCOUNT, TOTAL_TAX, TOTAL_VALUE):
    command = "INSERT INTO ac_invoices(ID, TENANT_ID, CUSTOMER_ID, DOC_DATE, DOC_NUMBER, TOTAL_DISCOUNT, TOTAL_TAX, TOTAL_VALUE) "
    values = "VALUES ({}, {}, {}, {}, {}, {}, {}, {});".format(ID,
                                                               TENANT_ID,
                                                               CUSTOMER_ID,
                                                               DOC_DATE,
                                                               DOC_NUMBER,
                                                               TOTAL_DISCOUNT,
                                                               TOTAL_TAX,
                                                               TOTAL_VALUE)
    cursor.execute(command + values)
    db.commit()



def crear_ac_products(ID, TENANT_ID, NAME, DESCRIPTION, LIST_PRICE):
    command = "INSERT INTO ac_products(ID, TENANT_ID, NAME, DESCRIPTION, LIST_PRICE) "
    values = "VALUES ({}, {}, {}, {}, {});".format(ID, TENANT_ID, NAME, DESCRIPTION, LIST_PRICE)
    cursor.execute(command + values)
    db.commit()


def crear_ac_tenant(ID, NAME):
    command = "INSERT INTO ac_tenant(ID, NAME) "
    values = "VALUES ({}, {});".format(ID, NAME)
    cursor.execute(command + values)
    db.commit()

def crear_customer(ID, TENANT_ID, FIRST_NAME, LAST_NAME):
    command = "INSERT INTO customer(ID, TENANT_ID, FIRST_NAME, LAST_NAME)) "
    values = "VALUES ({}, {}, {}, {});".format(ID, TENANT_ID, FIRST_NAME, LAST_NAME))
    cursor.execute(command + values)
    db.commit()
