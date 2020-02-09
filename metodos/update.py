#!/usr/bin/env python3

import MySQLdb


def update_table(ID, TABLE, PARAMS):
    db = MySQLdb.connect(host="localhost", user="electros", passwd="electros", db="siigo")
    cursor = db.cursor()
    try:
        st = str(PARAMS)
        st = st.replace(",", "")
        l = []
        st = st.split(" ")
        for i in st:
            l.append(i.split("="))
        dic = {}
        for i in l:
            dic[i[0]] = i[1]
            for key, val in dic.items():
                command = "UPDATE {} SET {}='{}'  WHERE id = {};".format(TABLE, key, val, ID)
                cursor.execute(command)
        db.commit()
        db.close()
        return {'message': 'Update {} in table {} with {}'.format(ID, TABLE, PARAMS)}
    except:
        db.close()
        return {'message': 'Can not update an unexisting id'}
