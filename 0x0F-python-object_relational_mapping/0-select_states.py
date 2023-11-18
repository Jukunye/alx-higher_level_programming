#!/usr/bin/python3
"""
This module list all states from the datagase
"""

import sys
import MySQLdb

if __name__ == "__main__":

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()
