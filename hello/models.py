from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    password = Column(String(20), unique=False)

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User: {}>'.format(
            self.name
        )
