from sqlmodel import Session, select
from app.models import Ram

def create_ram(session: Session, ram: Ram):
    session.add(ram)
    session.commit()
    session.refresh(ram)
    return ram

def get_ram(session: Session, ram_id: int):
    return session.get(Ram, ram_id)

def update_ram(session: Session, ram_id: int, ram_data: dict):
    db_ram = session.get(Ram, ram_id)
    if not db_ram:
        return None
    for key, value in ram_data.items():
        setattr(db_ram, key, value)
    session.add(db_ram)
    session.commit()
    session.refresh(db_ram)
    return db_ram

def delete_ram(session: Session, ram_id: int):
    db_ram = session.get(Ram, ram_id)
    if not db_ram:
        return None
    session.delete(db_ram)
    session.commit()
    return db_ram
