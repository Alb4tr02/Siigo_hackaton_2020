#!/usr/bin/env python3

import MySQLdb


def delete_row(ID, TABLE):
    db = MySQLdb.connect(host="localhost", user="electros", passwd="electros", db="siigo")
    cursor = db.cursor()
    try:
        command = "DELETE FROM {} WHERE id={}".format(TABLE, ID)
        cursor.execute(command)
        db.commit()
        db.close()
        return {'message': 'Delete {} on table: {}'.format(ID, TABLE)}
    except:
        db.close()
        return {'error': 'Can not delete an unexisting id'}
