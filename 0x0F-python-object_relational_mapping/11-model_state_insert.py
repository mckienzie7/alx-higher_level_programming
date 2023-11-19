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
    state_name = "Louisiana"
    state = State(name=state_name)
    session.add(state)
    session.commit()

    state_added = session.query(State).filter_by(name="Louisiana").first()
    print("{}".format(state_added.id))
