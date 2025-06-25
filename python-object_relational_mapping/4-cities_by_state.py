#!/usr/bin/python3
"""
This script retrieves all cities from the specified database and
displays the city ID, city name, and the name of the state to which the city belongs.
"""

import MySQLdb
import sys


def list_cities(username, password, database):
    """
    Retrieve all cities from the database and display them in ascending order by ID.
    """
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
    cursor = db.cursor()

    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states on cities.state_id = states.id
    ORDER BY cities.id ASC
    """

    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_cities(username, password, database)
