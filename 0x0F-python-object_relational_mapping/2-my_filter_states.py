#!/usr/bin/python3
"""
This script that takes in an argument and displays all values
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

    query = f"SELECT * \
                FROM states \
                WHERE states.name = '{sys.argv[4]}' \
                ORDER BY states.id ASC;"

    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()
