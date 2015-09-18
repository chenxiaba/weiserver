# APP   : Messnote Server v0.1 
# author: chenxiaba
# date  : 2015.09.15
import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Text,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Person(Base):
	"""docstring for Person"""
	__tablename__ = 'persion'
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	email = Column(String(64))

class Note(Base):
	"""docstring for Note"""
	__tablename__ = 'note'
	id = Column(Integer, primary_key=True)
	date = Column(DateTime)
	content = Column(Text)
	person_id = Column(Integer, ForeignKey('persion.id'))
	person = relationship(Person)

#Create dababase and table
engine = create_engine('sqlite:///messnote.db')
Base.metadata.create_all(engine)



