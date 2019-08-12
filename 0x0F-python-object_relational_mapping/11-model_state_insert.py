#!/usr/bin/python3
"""script that adds new State
'Louisiana' to the database"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                            .format(argv[1], argv[2], argv[3]), 
                            pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    newState = State(name="Louisiana")

    session.add(newState)

    state = session.query(State).filter_by(name='Louisiana').first()

    session.commit()

    print(state.id)
    session.close()
