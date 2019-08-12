#!/usr/bin/python3
"""Create California"""
import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    newState = State(name='California')
    newCity = City(name='San Francisco')

    newState = State(name="California")
    session.add(newState)
    session.commit()

    newCity = City(name="San Francisco", state_id=new_state.id)
    session.add(newCity)
    session.commit()
    session.close()
