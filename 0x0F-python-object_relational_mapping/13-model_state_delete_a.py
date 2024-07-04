#!/usr/bin/python3
"""Deletes all State objects with a name containing letter 'a'"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
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

    # Query and delete all State objects with name containing 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    # Close the session
    session.close()
