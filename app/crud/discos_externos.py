from sqlmodel import Session
from app.models import DiscosExternos

def create_discos_externos(session: Session, discos_externos: DiscosExternos):
    session.add(discos_externos)
    session.commit()
    session.refresh(discos_externos)
    return discos_externos

def get_discos_externos(session: Session, discos_externos_id: int):
    return session.get(DiscosExternos, discos_externos_id)

def update_discos_externos(session: Session, discos_externos_id: int, discos_externos_data: dict):
    db_discos_externos = session.get(DiscosExternos, discos_externos_id)
    if not db_discos_externos:
        return None
    for key, value in discos_externos_data.items():
        setattr(db_discos_externos, key, value)
    session.add(db_discos_externos)
    session.commit()
    session.refresh(db_discos_externos)
    return db_discos_externos

def delete_discos_externos(session: Session, discos_externos_id: int):
    db_discos_externos = session.get(DiscosExternos, discos_externos_id)
    if not db_discos_externos:
        return None
    session.delete(db_discos_externos)
    session.commit()
    return db_discos_externos
