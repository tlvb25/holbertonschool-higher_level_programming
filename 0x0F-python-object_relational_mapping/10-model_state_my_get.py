#!/usr/bin/python3
"""script lists State objects that contain
 the letter 'a' """
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    query = session.query(State)\
        .filter(State.name == sys.argv[4]).all()

    if query:
        print(query.id)
    else:
        print('Not found')
    session.close()
