#!/usr/bin/env python3

import MySQLdb


def delete_row(table_name, id):
    db = MySQLdb.connect(host="localhost", user="electros", passwd="electros", db="siigo")
    cursor = db.cursor()
    try:
        command = "DELETE FROM {} WHERE id={}".format(table_name, id)
        cursor.execute(command)
        db.commit()
        db.close()
        return {'message': 'Delete {} on table: {}'.format(id, table_name)}
    except:
        db.close()
        return {'message': 'Can not delete an unexisting id'}
