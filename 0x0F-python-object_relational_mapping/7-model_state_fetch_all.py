#!/usr/bin/python3
"""List all State objects from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_state import Base, State

    if len(argv) != 4:
        print(f"Usage: {argv[0]} <mysql username> <mysql password> <database name>")
        exit(1)

    username, password, db_name = argv[1], argv[2], argv[3]

    try:
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

        # Query all State objects and order by state id
        states = session.query(State).order_by(State.id).all()

        # Print results
        for state in states:
            print(f"{state.id}: {state.name}")

        # Close the session
        session.close()
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
