#!/usr/bin/python3
"""
This script that prints the first State object
from the database hbtn_0e_6_usa.
"""

from sys import argv
from model_state import Base, State
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

    state = session.query(State).order_by(State.id).first()

    if state is None:
        print('Nothing')
    else:
        print("{}: {}".format(state.id, state.name))

    session.close()
