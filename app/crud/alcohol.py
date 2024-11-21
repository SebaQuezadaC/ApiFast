from sqlmodel import Session
from app.models import Alcohol

def create_alcohol(session: Session, alcohol: Alcohol):
    session.add(alcohol)
    session.commit()
    session.refresh(alcohol)
    return alcohol

def get_alcohol(session: Session, alcohol_id: int):
    return session.get(Alcohol, alcohol_id)

def update_alcohol(session: Session, alcohol_id: int, alcohol_data: dict):
    db_alcohol = session.get(Alcohol, alcohol_id)
    if not db_alcohol:
        return None
    for key, value in alcohol_data.items():
        setattr(db_alcohol, key, value)
    session.add(db_alcohol)
    session.commit()
    session.refresh(db_alcohol)
    return db_alcohol

def delete_alcohol(session: Session, alcohol_id: int):
    db_alcohol = session.get(Alcohol, alcohol_id)
    if not db_alcohol:
        return None
    session.delete(db_alcohol)
    session.commit()
    return db_alcohol
