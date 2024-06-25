#!/usr/bin/python3
"""Print the first State object from the database"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sys import argv
    from model_state import Base, State
    from sqlalchemy.engine.url import URL

    # URL
    url = {
        'drivername': 'mysql+mysqldb',
        'host': 'localhost',
        'port': '3306',
        'username': argv[1],
        'password': argv[2],
        'database': argv[3]
    }

    c_url = URL(**url)

    # Create engine and metadata for stored objects
    engine = create_engine(c_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Session
    session = Session(engine)

    try:
        first = session.query(State).first()
        if first is not None:
            print("{}: {}".format(first.id, first.name))
        else:
            print("Nothing")
    except Exception as e:
        print(f"Error: {e}")

    # Close session
    session.close()
