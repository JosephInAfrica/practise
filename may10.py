from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()	

class User(object):
	__tablename__='user'
	def __init__(self,id,name):
		self.id=id
		self.name=name

	id=Column(String(20),primary_key=True)
	name=Column(String(20))

engine=create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
DBSession=sessionmaker(bind=engine)
