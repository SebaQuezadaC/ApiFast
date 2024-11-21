from sqlmodel import Session
from app.models import Refrigeracion

def create_refrigeracion(session: Session, refrigeracion: Refrigeracion):
    session.add(refrigeracion)
    session.commit()
    session.refresh(refrigeracion)
    return refrigeracion

def get_refrigeracion(session: Session, refrigeracion_id: int):
    return session.get(Refrigeracion, refrigeracion_id)

def update_refrigeracion(session: Session, refrigeracion_id: int, refrigeracion_data: dict):
    db_refrigeracion = session.get(Refrigeracion, refrigeracion_id)
    if not db_refrigeracion:
        return None
    for key, value in refrigeracion_data.items():
        setattr(db_refrigeracion, key, value)
    session.add(db_refrigeracion)
    session.commit()
    session.refresh(db_refrigeracion)
    return db_refrigeracion

def delete_refrigeracion(session: Session, refrigeracion_id: int):
    db_refrigeracion = session.get(Refrigeracion, refrigeracion_id)
    if not db_refrigeracion:
        return None
    session.delete(db_refrigeracion)
    session.commit()
    return db_refrigeracion
