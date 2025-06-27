#!/usr/bin/python3
"""
This module is used to connect to the database mysqldb.
"""


import MySQLdb
import sys


def list_states_with_N(username, password, database):
    """
    List the names of states that start with N
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
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states_with_N(username, password, database)
