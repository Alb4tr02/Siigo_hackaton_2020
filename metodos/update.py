#!/usr/bin/env python3

import MySQLdb


def update_table(table_name, id, data):
    db = MySQLdb.connect(host="localhost", user="electros", passwd="electros", db="siigo")
    cursor = db.cursor()
    try:
        for key, val in data.items():
            command = "UPDATE {} SET {}='{}'  WHERE {};".format(table_name, key, val, id)
            cursor.execute(command)
        db.commit()
        db.close()
        return {'message': 'Update {} in table {} with id={}'.format(id, table_name, data)}
    except:
        db.close()
        return {'error': 'Can not update an unexisting id'}
