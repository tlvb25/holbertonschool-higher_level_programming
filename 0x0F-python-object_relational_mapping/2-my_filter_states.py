#!/usr/bin/python3
"""script takes arguments and displays all rows in states table
that matches argv[4]"""
from sys import argv
import MySQLdb


if __name__ == '__main__':
    user, password, database, state = argv[1], argv[2], argv[3], argv[4]
    db = MySQLdb.connect(host="localhost",
                         user=user, passwd=password, db=database)
    cur = db.cursor()
    cur.execute(
        """SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id"""
        .format(state))
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    db.close()
