#!/usr/bin/python3
"""script lists all states name beg "N" from db hbtn_0e_0_usa"""
import MySQLdb
from sys import argv


if __name__ == "__main__":

    # storing entire database connection into variable 'db'
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         charset="utf-8",
                         user=argv[1],
                         passwd=argv[2],  # using argv[] variables directly
                         db=argv[3])     # using argv[] variables directly

    # must use databse cursor obj in order to execute queries
    cur = db.cursor()

    # # HERE I have to know SQL to grab all states in my database
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC",
        (argv[4], ))

    # all rows in the states table
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    db.close()