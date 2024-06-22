#!/usr/bin/python3
"""script that lists all states from a database"""


from sys import argv
import MySQLdb


if __name__ == "__main__":
    dic = {
        'host': "localhost",
        'port': 3306,
        'user': argv[1],
        'passwd': argv[2],
        'db': argv[3]
    }
    command = "select * from states order by id"

    db = MySQLdb.connect(**dic)
    cursor = db.cursor()
    cursor.execute(command)

    results = cursor.fetchall()
    for dates in results:
        print(dates)

    cursor.close()
    db.close()