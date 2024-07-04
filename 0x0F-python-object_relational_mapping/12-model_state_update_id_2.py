#!/usr/bin/python3
"""Changes the name of a State object from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
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

    # Query for the State object with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Check if the state exists and update its name
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
