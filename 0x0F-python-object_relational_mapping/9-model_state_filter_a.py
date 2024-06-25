#!/usr/bin/python3
"""Print the State object with the name passed as argument from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    from model_state import Base, State
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    if len(argv) != 5:
        print(f"Usage: {argv[0]} <mysql username> <mysql password> <database name> <state name>")
        exit(1)

    username, password, db_name, state_name = argv[1], argv[2], argv[3], argv[4]

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

    # Query for the State object with the specified name
    state = session.query(State).filter(State.name == state_name).first()

    # Print result
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    # Close the session
    session.close()
