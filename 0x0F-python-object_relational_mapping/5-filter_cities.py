#!/usr/bin/python3
"""script lists all states name beg "N" from db hbtn_0e_0_usa"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    user, password, database, state = argv[1], argv[2], argv[3], argv[4]
    db = MySQLdb.connect(host="localhost",
                         user=user, passwd=password, db=database)

    cur = db.cursor()

    cur.execute("""
    SELECT cities.name
    FROM cities
    JOIN states
    ON state_id=states.id
    WHERE states.name LIKE BINARY %s
    ORDER BY cities.id
    """, (state,))

    query = cur.fetchall()
    print(", ".join([row[0] for row in query]))
    cur.close()
    db.close()
