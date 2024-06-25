#!/usr/bin/python3
"""Prints all City objects from the database"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from model_city import City
    from sys import argv

    if len(argv) != 4:
        print(f"Usage: {argv[0]} <mysql username> <mysql password> <database name>")
        exit(1)

    username, password, db_name = argv[1], argv[2], argv[3]

    # Create the database engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all City objects joined with State and sorted by city id
    query = session.query(State.name, City)\
                   .filter(State.id == City.state_id)\
                   .order_by(City.id).all()

    # Print results
    for state_name, city in query:
        print(f"{state_name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
