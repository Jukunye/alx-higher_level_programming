#!/usr/bin/python3
"""
This script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = (
        session.query(State)
        .outerjoin(City)
        .order_by(State.id, City.id).all()
    )

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for citi in state.cities:
            print("    {}: {}".format(citi.id, citi.name))

    session.close()
