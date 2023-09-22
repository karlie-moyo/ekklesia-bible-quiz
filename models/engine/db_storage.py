#!/usr/bin/env python3
"""SQLAlchemy Storage Engine"""
from models.user import User
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv
from dotenv import load_dotenv
from models.answer import Answer
from models.question import Question
from models.result import Result

load_dotenv()

# grouping of models' classes
classes = [Answer, Question, Result, User]
DB_USER = getenv('DB_USER')
DB_PWD = getenv('DB_PWD')
DB_HOST = getenv('DB_HOST')
DB_NAME = getenv('DB_NAME')
DB_ENGINE = getenv('DB_ENGINE')

# check if the running instance is a test environment
TEST = getenv('TEST')
if TEST == 'True':
    DB_ENGINE = 'sqlite'
    DB_NAME = 'tests'

# create database connection
engine = None
if DB_ENGINE == 'mysql':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@{}/{}'.format(
            DB_USER, DB_PWD, DB_HOST, DB_NAME
        ),
        pool_pre_ping=True,
        pool_recycle=3600
    )
else:
    engine = create_engine(
        'sqlite:///{}.sqlite'.format(DB_NAME),
        pool_pre_ping=True
    )


class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """DBStorage class constructor"""
        self.__engine = engine

    def reload(self):
        """(Re)load data from MySQL database"""
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(factory)

    def new(self, obj):
        """Add `obj` to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Save/commit all changes of the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete `obj` from database"""
        if obj is not None:
            self.__session.delete(obj)

    def rollback(self):
        """rolls back the current Sqlalchemy session
        after a failed flush occured
        just for testing purposes"""
        self.__session.rollback()

    def all(self, cls=None):
        """
        query-> SELECT * FROM cls.__tablename__
        [Returns a dictionary (key:obj) object for easy indexing]
        """
        objs_dict = {}
        if cls is None:
            for item in classes:
                objs = self.__session.query(item).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    objs_dict[key] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                objs_dict[key] = obj

        return objs_dict

    def close(self):
        """close the current db session"""
        self.__session.remove()

    def get(self, cls, id, attr=None):
        """
        Returns a `obj` of `cls` with a matching `id`,
        or None if not exists.
        """
        if cls not in classes:
            return None
        if attr is not None:
            obj = self.all(cls).get(cls.__name__ + '.' + id, None)
            if obj is None:
                return obj
            return getattr(obj, attr, None)
        return self.all(cls).get(cls.__name__ + '.' + id, None)

    def match(self, cls, all=False, **kwargs):
        """
        Returns a `obj` of `cls` with a matching list
        of attributes
        """
        from sqlalchemy import func
        if cls not in classes or len(kwargs) == 0:
            return None
        results = []
        for key, value in kwargs.items():
            if all is False:
                obj = self.__session.query(cls).filter(
                    func.lower(getattr(cls, key)) == value.lower()).first()
                if obj is not None:
                    return obj
            else:
                obj = self.__session.query(cls).filter(
                    func.lower(getattr(cls, key)) == value.lower()).all()
                if obj is not None:
                    results.extend(obj)
                    obj = results[:]
        return obj
