#!/usr/bin/python3
"""DataBase Storage Engine"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os
from models.base_model import Base, BaseModel
from models import city, place, review, state, amenity, user


class DBStorage:
    """DataBase Storage"""
    __engine = None
    __session = None
    classes = {
        'City': city.City,
        'Place': place.Place,
        'Review': review.Review,
        'State': state.State,
        'Amenity': amenity.Amenity,
        'User': user.User
    }


    def __init__(self):
        """DBStorage Class"""
        from models.base_model import Base

        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        database = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the database"""
        if cls is None:
            temp = []
            for c in self.__all_classes.values():
                temp.extend(self.__session.query(c).all())
        else:
            if type(cls) is str:
                cls = self.__all_classes.get(cls.lower())
                if cls is None:
                    return {}
            temp = self.__session.query(cls).all()
        new_dict = {}
        for obj in temp:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """Adds the object to the current database"""
        self.__session.add(obj)

    def save(self):
        """Saves the current database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from current database"""
        if obj is not None:
            self.__session.delete(obj)
        else:
            pass

    def reload(self):
        """ Recreate the current database"""
        Base.metadata.create_all(self.__engine)
        the_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(the_session)
        self.__session = Session()

    def close(self):
        """End"""
        self.__session.remove()
