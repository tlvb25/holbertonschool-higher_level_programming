#!/usr/bin/python3
"""script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa"""
from sys import argv
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    # storing imported State Object into variable state
    state = State(name='Louisiana')
    # adding the State Object to database
    session.add(state)

    session.commit()
    print(state.id)
    session.close()
