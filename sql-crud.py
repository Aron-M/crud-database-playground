from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the "Programmer" table
class Cities(base): 
    __tablename__ = "Cities"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    country = Column(String)
    rating = Column(String)
    food = Column(String)
    famous_for = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on our Cities table