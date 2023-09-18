#!/usr/bin/python3
"""
model_state.py:
Define the State class and create the corresponding table in a MySQL database.
"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a declarative base instance
Base = declarative_base()

# Define the State class
class State(Base):
    """Represents a state in a database table.

    This class defines the structure of a 'states' table in a MySQL database.
    It includes two attributes:
    - id (int): An auto-generated unique identifier for the state.
    - name (str): The name of the state with a maximum length of 128 characters.

    Attributes:
        __tablename__ (str): The name of the database table associated with this class.
        id (Column): An integer column representing the primary key of the state.
        name (Column): A string column representing the name of the state.

    Args:
        Base (declarative_base): The SQLAlchemy declarative base instance to inherit from.

    Note:
        All instances of this class are expected to be stored in a 'states' table in the database.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Create the database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create the table in the database
    Base.metadata.create_all(engine)

    print("Table 'states' created successfully.")
