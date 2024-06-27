#!/usr/bin/python3
"""Script to list all State objects and corresponding City objects"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./101-relationship_states_cities_list.py <mysql username> <mysql password> <database name>")
        exit(1)

    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    session.close()
