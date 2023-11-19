#!/usr/bin/python3
"""
This script lists all State objects
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the states and cities
    from the database.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = (
        session.query(City.id, City.name, State.name)
        .join(State, City.state_id == State.id)
        .order_by(City.id.asc()).all()
    )

    for city_id, city_name, state_name in result:
        print("{}: ({}) {}".format(state_name, city_id, city_name))

    session.close()
