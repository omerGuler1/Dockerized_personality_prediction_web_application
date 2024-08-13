from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Prediction(Base):
    __tablename__ = 'predictions'
    
    id = Column(Integer, primary_key=True, index=True)
    personality_type = Column(String(50), index=True)
    # name = Column(String(50), index=True)
    # surname = Column(String(50), index=True)

class PredictionDetails(Base):
    __tablename__ = 'prediction_details'
    
    id = Column(Integer, primary_key=True, index=True)
    personality_type = Column(String(50), index=True)
    
    for i in range(1, 61):
        locals()[f'q{i}'] = Column(Integer)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    name = Column(String(50), index=True)
    surname = Column(String(50), index=True)
    gender = Column(String(50), index=True)


class Feedback(Base):
    __tablename__ = 'feedbacks'

    id = Column(Integer, primary_key=True, index=True)
    feedback = Column(String(255), index=True)
    prediction = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)