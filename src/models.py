import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_name = Column(String(15), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)

    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "user_name": self.user_name,
    #         "email": self.email
    #     }


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    id_planets = Column(Integer, ForeignKey('planets.id'))
    id_characters = Column(Integer, ForeignKey('characters.id'))
    id_ships = Column(Integer, ForeignKey('ships.id'))  
    


class Characters(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    gender = Column(String(15))
    sharship = Column(String(100), ForeignKey('ships.id'))
    homeworld = Column(String(250), ForeignKey('planets.id'))


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)


class Ships(Base):
    __tablename__ = 'ships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')