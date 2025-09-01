from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    score = Column(Integer, default=0)
    badges = Column(String, default='')  # comma-separated
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    progress = relationship('Progress', back_populates='user')

class Progress(Base):
    __tablename__ = 'progress'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    stage = Column(Integer, default=1)
    level = Column(Integer, default=1)
    completed_missions = Column(String, default='')  # comma-separated
    achievements = Column(String, default='')  # comma-separated
    user = relationship('User', back_populates='progress')

class Mission(Base):
    __tablename__ = 'missions'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    stage = Column(Integer)
    level = Column(Integer)
    skill_type = Column(String)  # e.g. algorithms, data structures
    is_timed = Column(Boolean, default=False)
    time_limit = Column(Integer, default=0)  # seconds
    hurdle = Column(String, default='')

class Leaderboard(Base):
    __tablename__ = 'leaderboard'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    score = Column(Integer, default=0)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
