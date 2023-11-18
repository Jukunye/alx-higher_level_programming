#!/usr/bin/python3
"""
 script that takes in the name of a state as an argument
 and lists all cities of that state
"""

import sys
import MySQLdb

search = sys.argv[4]

if __name__ == "__main__":

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = connection.cursor()

    query = "SELECT cities.id, cities.name, states.name \
            FROM cities \
           INNER JOIN states \
           ON cities.state_id = states.id \
           ORDER BY cities.id ASC;"

    cursor.execute(query)
    rows = cursor.fetchall()

    print(", ".join(f"{city}" for id, city, state in rows if state == search))

    cursor.close()
    connection.close()
