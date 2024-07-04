#!/usr/bin/python3
"""Script to list all City objects from the database"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.engine.url import URL
    from relationship_city import City
    from relationship_state import Base, State
    from sys import argv

    db = {
        'drivername': 'mysql+mysqldb',
        'host': 'localhost',
        'port': '3306',
        'username': argv[1],
        'password': argv[2],
        'database': argv[3]
    }

    url = URL(**db)
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for city in session.query(City).order_by(City.id).all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
