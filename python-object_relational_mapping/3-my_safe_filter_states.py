#!/usr/bin/python3
"""
This script safely retrieves and displays records from
the database that match the provided state name,
protecting against SQL injection attacks.
"""


import MySQLdb
import sys


def safe_filter_states_by_name(username, password, database, state_name):
    """
    Display all values in the states table where
    name matches the argument.
    """
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    safe_filter_states_by_name(username, password, database, state_name)
