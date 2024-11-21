from sqlmodel import Session
from app.models import PlacaBase

def create_placa_base(session: Session, placa_base: PlacaBase):
    session.add(placa_base)
    session.commit()
    session.refresh(placa_base)
    return placa_base

def get_placa_base(session: Session, placa_base_id: int):
    return session.get(PlacaBase, placa_base_id)

def update_placa_base(session: Session, placa_base_id: int, placa_base_data: dict):
    db_placa_base = session.get(PlacaBase, placa_base_id)
    if not db_placa_base:
        return None
    for key, value in placa_base_data.items():
        setattr(db_placa_base, key, value)
    session.add(db_placa_base)
    session.commit()
    session.refresh(db_placa_base)
    return db_placa_base

def delete_placa_base(session: Session, placa_base_id: int):
    db_placa_base = session.get(PlacaBase, placa_base_id)
    if not db_placa_base:
        return None
    session.delete(db_placa_base)
    session.commit()
    return db_placa_base
