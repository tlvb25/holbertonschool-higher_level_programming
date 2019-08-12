#!/usr/bin/python3
"""create state california and city"""
from sys import argv
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import City, Base


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
                 
    Base.metadata.create_all(engine)

    session = Session(engine)

    state = State(name="California")
    session.add(state)
    session.commit()
    city = City(name="San Francisco", state_id=new_state.id)
    session.add(city)
    session.commit()
    session.close()
