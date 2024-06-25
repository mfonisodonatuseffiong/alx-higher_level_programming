#!/usr/bin/python3
"""Print the first State object from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_state import Base, State

    if len(argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(argv[0]))
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

    try:
        first_state = session.query(State).order_by(State.id).first()
        if first_state:
            print(f"{first_state.id}: {first_state.name}")
        else:
            print("Nothing")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()
