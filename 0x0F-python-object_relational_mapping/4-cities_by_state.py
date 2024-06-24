#!/usr/bin/python3
"""Lists all cities from database"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # Connect to the database
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # Create a cursor object
    c = db.cursor()

    # Execute the query
    cmd = (
        "SELECT cities.id, cities.name, states.name "
        "FROM cities JOIN states ON cities.state_id = states.id"
    )
    c.execute(cmd)

    # Fetch all rows
    rows = c.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the cursor and connection
    c.close()
    db.close()
