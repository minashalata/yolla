from sqlalchemy import Column, Integer, String, Boolean,ForeignKey, Unicode
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

# Your Code Below:
Base = declarative_base()
class User(Base):
   __tablename__ = 'user'
   id = Column(Integer, primary_key= True)
   username = Column(String)
   passward = Column(String)



