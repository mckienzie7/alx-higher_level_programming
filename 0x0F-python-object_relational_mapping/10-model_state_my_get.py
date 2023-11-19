#!/usr/bin/python3
"""
Query from database table
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True
            )
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    state = session.query(State)\
        .filter_by(name=sys.argv[4])\
        .order_by(State.id)\
        .first()
    if state is not None:
        print(state.id)
    else:
        print("Not found")
