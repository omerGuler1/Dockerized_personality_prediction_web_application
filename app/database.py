from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from dotenv import load_dotenv
from sqlmodel import create_engine

load_dotenv() # take environment variables from .env.

DB_URL = os.getenv("DATABASE_URL")
engine = create_engine(DB_URL,echo=True)
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base = declarative_base()

def init_db():
    import models
    inspector = inspect(engine)
    tables = inspector.get_table_names()

    if 'predictions' not in tables:
        models.Prediction.__table__.create(bind=engine)
    if 'prediction_details' not in tables:
        models.PredictionDetails.__table__.create(bind=engine)
    if 'users' not in tables:
        models.User.__table__.create(bind=engine)
    if 'feedbacks' not in tables:
        models.Feedback.__table__.create(bind=engine)