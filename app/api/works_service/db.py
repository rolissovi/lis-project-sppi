import os

from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

worker = Table(
    'worker',
    metadata,
    Column('worker_sk', Integer, primary_key=True),
    Column('permission_sk', Integer),
    Column('login', String(50)),
    Column('password', String(50)),
)

user = Table(
    'user',
    metadata,
    Column('user_sk', Integer, primary_key=True),
)

permission = Table(
    'permission',
    metadata,
    Column('permission_sk', Integer, primary_key=True),
)

client = Table(
    'client',
    metadata,
    Column('client_sk', Integer, primary_key=True),
    Column('permission_sk', Integer),
    Column('login', String(50)),
    Column('password', String(50)),
)

database = Database(DATABASE_URI)