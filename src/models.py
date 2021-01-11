import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__='user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    fristname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)

class Post(Base):
    __tablename__='post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    text = Column(String(250), nullable=False)
    user = relationship(User)
    

class Media(Base):
    __tablename__='media'
    id =  Column(Integer, primary_key=True)
    type_media = Column(Integer, nullable=False)
    url = Column(String(250), nullable=False)
    id_post = Column(Integer, ForeignKey('post.id'))
    post= relationship(Post)

class Comment(Base):
    __tablename__='comment'
    id = Column(Integer, primary_key=True)
    comment_tex = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    user = relationship(User)
    post = relationship(Post)

class Follower(Base):
    __tablename__='follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

  

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')