#!/usr/bin/python3
"""script changes the name of a State"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    states = session.query(State).filter(State.id == 2).all()

    if states:
        states[0].name = "New Mexico"
    session.commit()
    session.close()
