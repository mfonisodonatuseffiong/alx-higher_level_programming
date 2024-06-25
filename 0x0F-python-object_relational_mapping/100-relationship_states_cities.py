#!/usr/bin/python3
"""Script to create City and State objects"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.engine.url import URL
    from relationship_city import City
    from relationship_state import Base, State
    from sys import argv

    if len(argv) != 4:
        print(f"Usage: {argv[0]} <mysql username> <mysql password> <database name>")
        exit(1)

    username, password, db_name = argv[1], argv[2], argv[3]

    # Database connection URL
    db_url = URL(drivername='mysql+mysqldb',
                 username=username,
                 password=password,
                 host='localhost',
                 port=3306,
                 database=db_name)

    # Create engine and bind session
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create City and State objects
    city = City(name='San Francisco')
    state = State(name='California', cities=[city])

    # Add objects to session, commit changes, and close session
    session.add(state)
    session.add(city)
    session.commit()
    session.close()
