#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from models import storage
from os import getenv
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class.

        Attributes:
                  __tablename__ (str): Name of MySQL table to store States
                  name (string): The name of the State (128 characters)
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            all_cities = list(storage.all(City).values())
            return [city for city in all_cities if city.state_id == self.id]
