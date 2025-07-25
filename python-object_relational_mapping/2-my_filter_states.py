#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""


import MySQLdb
import sys


def filter_states_by_name(username, password, database, state_name):
    """
    Display all values in the states table where
    name matches the argument.
    """
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
        )

    cursor = db.cursor()
    query = (
        "SELECT * FROM states WHERE name = BINARY '{}'"
        "ORDER BY id ASC"
    ).format(state_name)
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
    state_name = sys.argv[4]

    filter_states_by_name(username, password, database, state_name)
