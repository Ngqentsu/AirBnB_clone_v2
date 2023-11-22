#!/usr/bin/python3
"""Defines the DBStorage engine."""

from models.base_model import BaseModel
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


class DBStorage:
    """Manages the storage of hbnb models in a database.

    Attributes:
              __engine (): The working SQLAlchemy engine.
              __session (): The working SQLAlchemy session.
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initializing a new DBStorage instance."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on current database session of all objects of the class."""

        if cls is not None:
            if isinstance(cls, str):
                cls = globals().get(cls, None)
            if cls:
                objects = self.__session.query(cls).all()
            else:
                return {}
        else:
            classes_to_query = (User, State, City, Amenity, Place, Review)
            objects = self.__session.query(*classes_to_query).all()

        return {"{}.{}".format(type(i).__name__, i.id): i for i in objects}

    def new(self, obj):
        """Add object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.close()


if __name__ == "__main__":
    storage.reload()
