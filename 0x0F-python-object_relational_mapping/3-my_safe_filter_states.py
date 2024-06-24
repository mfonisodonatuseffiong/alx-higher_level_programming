#!/usr/bin/python3
"""Filter states by user input"""

import MySQLdb
from sys import argv

def main():
    if len(argv) == 5:
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
        c.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id ASC", (argv[4],))
        
        # Fetch all rows
        rows = c.fetchall()
        
        # Print the rows
        for row in rows:
            print(row)
        
        # Close the cursor and connection
        c.close()
        db.close()
    else:
        return

if __name__ == "__main__":
    main()
