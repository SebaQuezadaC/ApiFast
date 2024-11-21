from sqlmodel import Session, select
from app.models import Microfono

def create_microfono(session: Session, microfono: Microfono):
    session.add(microfono)
    session.commit()
    session.refresh(microfono)
    return microfono

def get_microfono(session: Session, microfono_id: int):
    return session.get(Microfono, microfono_id)

def update_microfono(session: Session, microfono_id: int, microfono_data: dict):
    db_microfono = session.get(Microfono, microfono_id)
    if not db_microfono:
        return None
    for key, value in microfono_data.items():
        setattr(db_microfono, key, value)
    session.add(db_microfono)
    session.commit()
    session.refresh(db_microfono)
    return db_microfono

def delete_microfono(session: Session, microfono_id: int):
    db_microfono = session.get(Microfono, microfono_id)
    if not db_microfono:
        return None
    session.delete(db_microfono)
    session.commit()
    return db_microfono