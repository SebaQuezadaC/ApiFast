from sqlmodel import Session
from app.models import Switch

def create_switch(session: Session, switch: Switch):
    session.add(switch)
    session.commit()
    session.refresh(switch)
    return switch

def get_switch(session: Session, switch_id: int):
    return session.get(Switch, switch_id)

def update_switch(session: Session, switch_id: int, switch_data: dict):
    db_switch = session.get(Switch, switch_id)
    if not db_switch:
        return None
    for key, value in switch_data.items():
        setattr(db_switch, key, value)
    session.add(db_switch)
    session.commit()
    session.refresh(db_switch)
    return db_switch

def delete_switch(session: Session, switch_id: int):
    db_switch = session.get(Switch, switch_id)
    if not db_switch:
        return None
    session.delete(db_switch)
    session.commit()
    return db_switch
