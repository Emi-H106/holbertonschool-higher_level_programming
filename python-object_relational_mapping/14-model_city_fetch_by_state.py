#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_14_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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

    results = session.query(State, City).join(City).order_by(City.id).all()

    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
