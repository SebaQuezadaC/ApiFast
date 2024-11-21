from sqlmodel import Session
from app.models import AireComprimido

def create_aire_comprimido(session: Session, aire_comprimido: AireComprimido):
    session.add(aire_comprimido)
    session.commit()
    session.refresh(aire_comprimido)
    return aire_comprimido

def get_aire_comprimido(session: Session, aire_comprimido_id: int):
    return session.get(AireComprimido, aire_comprimido_id)

def update_aire_comprimido(session: Session, aire_comprimido_id: int, aire_comprimido_data: dict):
    db_aire_comprimido = session.get(AireComprimido, aire_comprimido_id)
    if not db_aire_comprimido:
        return None
    for key, value in aire_comprimido_data.items():
        setattr(db_aire_comprimido, key, value)
    session.add(db_aire_comprimido)
    session.commit()
    session.refresh(db_aire_comprimido)
    return db_aire_comprimido

def delete_aire_comprimido(session: Session, aire_comprimido_id: int):
    db_aire_comprimido = session.get(AireComprimido, aire_comprimido_id)
    if not db_aire_comprimido:
        return None
    session.delete(db_aire_comprimido)
    session.commit()
    return db_aire_comprimido
