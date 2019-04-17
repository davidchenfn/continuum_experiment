import sqlalchemy as sa
from sqlalchemy import inspect, Column, BigInteger
from sqlalchemy.orm import sessionmaker
from sqlalchemy_continuum import make_versioned


def add_versioning(cls, engine):
    '''
    Add versioning to a table
    :param cls: class representing table
    :return: new class
    '''
    make_versioned(user_cls=None)
    args = ({ 'extend_existing': True },)
    new_cls = type(cls.__name__, cls.__bases__, {
        "__versioned__": {},
        "__tablename__": cls.__tablename__,
        "__table_args__": args
    })
    # primary_keys = inspect(cls).primary_key
    # if len(primary_keys) > 0:
    #     setattr(new_cls, primary_keys[0].key, primary_keys[0])
    sa.orm.configure_mappers()
    cls.metadata.create_all(engine)
    return cls