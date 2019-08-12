#!/usr/bin/python3
"""State matching argv[4]"""

from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = session(engine)
    query = session.query(State)\
            .filter(State.name == argv[4]).order_by(State.id).all()

    if query:
        print(query.id)
    else:
        print("Not found")
    session.close()
