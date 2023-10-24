import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id=Column(Integer(), primary_key=True)
    username=Column(String(30), nullable=False, unique=True)
    name =Column(String(80), nullable=False)
    lastname=Column(String(80), nullable=False)
    age=Column(Integer(), nullable=True)
    email=Column(String(80), nullable=True)
    country=Column(String(60), nullable=True)
    posts = relationship('Post', backref='users')
    comments = relationship('Comment', backref='users')


  

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer(), primary_key=True)
    user_id= Column(Integer(), ForeignKey('user.id'))
    content= Column(String(), nullable=False)
    saved = relationship('saved')


class Media(Base):
    __tablename__= 'media'
    id= Column(Integer(), primary_key=True)
    type= Column(String(30), nullable=False)
    user_id= Column(Integer(), ForeignKey('user.id'))

class Saved(Base):
    __tablename__='saved'
    id=Column(Integer(), primary_key=True)
    post_id= Column(Integer(), ForeignKey('post.id'))
    media_id= Column(Integer(), ForeignKey('media.id'))

class Comment(Base):
    __tablename__= 'comments'
    id= Column(Integer(), primary_key=True)
    comment= Column(String(250), nullable=False)
    user_id= Column(Integer(), ForeignKey('user.id'))
    post_id= Column(Integer(), ForeignKey('post.id'))
    
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
