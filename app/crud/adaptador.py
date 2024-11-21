from sqlmodel import Session
from app.models import Adaptador

def create_adaptador(session: Session, adaptador: Adaptador):
    session.add(adaptador)
    session.commit()
    session.refresh(adaptador)
    return adaptador

def get_adaptador(session: Session, adaptador_id: int):
    return session.get(Adaptador, adaptador_id)

def update_adaptador(session: Session, adaptador_id: int, adaptador_data: dict):
    db_adaptador = session.get(Adaptador, adaptador_id)
    if not db_adaptador:
        return None
    for key, value in adaptador_data.items():
        setattr(db_adaptador, key, value)
    session.add(db_adaptador)
    session.commit()
    session.refresh(db_adaptador)
    return db_adaptador

def delete_adaptador(session: Session, adaptador_id: int):
    db_adaptador = session.get(Adaptador, adaptador_id)
    if not db_adaptador:
        return None
    session.delete(db_adaptador)
    session.commit()
    return db_adaptador
