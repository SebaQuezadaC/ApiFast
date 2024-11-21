from sqlmodel import Session
from app.models import Teclado

def create_teclado(session: Session, teclado: Teclado):
    session.add(teclado)
    session.commit()
    session.refresh(teclado)
    return teclado

def get_teclado(session: Session, teclado_id: int):
    return session.get(Teclado, teclado_id)

def update_teclado(session: Session, teclado_id: int, teclado_data: dict):
    db_teclado = session.get(Teclado, teclado_id)
    if not db_teclado:
        return None
    for key, value in teclado_data.items():
        setattr(db_teclado, key, value)
    session.add(db_teclado)
    session.commit()
    session.refresh(db_teclado)
    return db_teclado

def delete_teclado(session: Session, teclado_id: int):
    db_teclado = session.get(Teclado, teclado_id)
    if not db_teclado:
        return None
    session.delete(db_teclado)
    session.commit()
    return db_teclado
