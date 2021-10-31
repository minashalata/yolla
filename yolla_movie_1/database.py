from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import *

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def create_user(username, password):
	user= User(username= username, passward= password)
	session.add(user)
	session.commit()

def query_by_name(username):
   user = session.query(
       User).filter_by(
       username=username).first()
   return user

