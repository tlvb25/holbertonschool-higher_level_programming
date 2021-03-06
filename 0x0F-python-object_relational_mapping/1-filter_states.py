#!/usr/bin/python3
"""Lists all states starting with 'N' """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states
    WHERE name LIKE BINARY 'N%' ORDER BY id""")
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    conn.close()
