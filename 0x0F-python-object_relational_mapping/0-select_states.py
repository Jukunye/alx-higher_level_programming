#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    try:
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

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL database: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
