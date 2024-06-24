#!/usr/bin/python3
"""Filter states by user input"""

import MySQLdb
from sys import argv


def main():
    """Main function to connect to the database and fetch states by user input"""
    # connect
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # cursor
    c = db.cursor()

    # execute query
    c.execute("SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC", (argv[4],))

    # fetch
    rows = c.fetchall()

    # print
    for row in rows:
        print(row)

    # close
    c.close()
    db.close()


if __name__ == "__main__":
    main()
