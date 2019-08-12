#!/usr/bin/python3
"""Create California"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    newState = State(name='California')
    newCity = City(name='San Francisco')
    newCity.cities.append(newCity)
    session.add(newState)
    session.add(newCity)
    session.commit()
    session.close()
