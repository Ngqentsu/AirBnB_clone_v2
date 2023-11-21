#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
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
