#!/usr/bin/python3
"""script that deletes states whose name includes
the letter 'a' """
import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    query = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for row in query:
        session.delete(row)
    session.commit()
    session.close()
