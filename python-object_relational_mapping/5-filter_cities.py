#!/usr/bin/python3
"""
This script retrieves and displays all cities from the database
that match the specified state name
"""


import MySQLdb
import sys


def list_cities_by_states(username, password, database, state_name):
    """
    Retrieve all cities that match the specified state name and
    display them in ascending order by ID.
    """
    try:
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

    cursor = db.cursor()
    query = """
    SELECT cities.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))
    results = cursor.fetchall()
    cities_list = [row[0] for row in results]
    cities_list_result = ", ", end="".join(cities_list)
    print(cities_list_result)

    except MySQLdb.Error as e:
    print(f"Error connecting to MySQL: {e}")

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    list_cities_by_states(username, password, database, state_name)
