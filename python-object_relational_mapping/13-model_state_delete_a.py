#!/usr/bin/python3
"""
Deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """Get command line arguments"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                username, password, db_name
            ),
            pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    delete_states = (
            session.query(State)
            .filter(State.name.like('%a%'))
            .all()
    )
    for state in delete_states:
        session.delete(state)

    session.commit()

    session.close()
