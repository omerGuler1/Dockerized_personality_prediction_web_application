from sqlalchemy.orm import Session
import models, schemas 

def create_user(db: Session, user: schemas.UserCreate):
    # fake_hashed_password = user.password + "97312467euhwfhquJSKDANF"
    db_user = models.User(email=user.email, password=user.password, name=user.name, surname=user.surname, gender=user.gender)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_feedback(db: Session, feedback_id: int):
    return db.query(models.Feedback).filter(models.Feedback.id == feedback_id).first()

def get_feedbacks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Feedback).offset(skip).limit(limit).all()

def create_feedback(db: Session, feedback: schemas.FeedbackCreate):
    db_feedback = models.Feedback(feedback=feedback.feedback, prediction=feedback.prediction)
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback

def delete_feedback(db: Session, feedback_id: int):
    db_feedback = db.query(models.Feedback).filter(models.Feedback.id == feedback_id).first()
    if db_feedback:
        db.delete(db_feedback)
        db.commit()
        return db_feedback
    return None

def update_feedback(db: Session, feedback_id: int, feedback_update: schemas.FeedbackBase):
    db_feedback = db.query(models.Feedback).filter(models.Feedback.id == feedback_id).first()
    if db_feedback:
        for key, value in feedback_update.dict().items():
            setattr(db_feedback, key, value)
        db.commit()
        db.refresh(db_feedback)
        return db_feedback
    return None
