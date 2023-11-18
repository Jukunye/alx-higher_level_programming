#!/usr/bin/python3
"""
This script that takes in an argument and displays all values
"""

import sys
import MySQLdb

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = connection.cursor()

    query = "SELECT * \
                FROM states \
                WHERE name LIKE BINARY '{}' \
                ORDER BY states.id ASC;".format(sys.argv[4])

    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()
