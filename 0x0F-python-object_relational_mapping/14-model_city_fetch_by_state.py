#!/usr/bin/python3
"""script that lists all states from database"""
from sys import argv
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_city import City
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    query = session.query(City, State)\
        .filter(State.id == City.state_id)\
        .order_by(City.id).all()

    for city, state in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
