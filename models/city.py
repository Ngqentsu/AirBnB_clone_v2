#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String


class City(BaseModel, Base):
    """ The city class, contains state ID and name.

        Attributes:
                  __tablename__ (str): Name of MySQL table to store Cities
                  name (string): The name of the City (128 characters)
                  state_id (string): The state id of the City (60 characters)
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
