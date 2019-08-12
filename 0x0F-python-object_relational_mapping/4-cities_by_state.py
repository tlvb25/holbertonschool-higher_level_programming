#!/usr/bin/python3
"""script lists all states name beg "N" from db hbtn_0e_0_usa"""
import MySQLdb
from sys import argv


if __name__ == "__main__":

    # assigning the 3 parameters to argv[]
    user, password, database = argv[1], argv[2], argv[3]

    #storing entire database connection into variable 'db'
    db = MySQLdb.connect(host=localhost,
                         port=3306,
                         user=user,
                         passwd=password,
                         db=database)

    # must use databse cursor obj in order to execute queries
    cur = db.cursor()

    # # HERE I have to know SQL to grab all states in my database
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities" +
                "INNER JOIN states ON cities.state_id=states.id" + 
                "ORDER BY cities.id")

    # all rows in the states table
    query_rows = cur.fetchall()
    count = 0
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
