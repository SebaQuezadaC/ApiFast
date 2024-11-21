from sqlmodel import Session, select
from app.models import Monitor

def create_monitor(session: Session, monitor: Monitor):
    session.add(monitor)
    session.commit()
    session.refresh(monitor)
    return monitor

def get_monitor(session: Session, monitor_id: int):
    return session.get(Monitor, monitor_id)

def update_monitor(session: Session, monitor_id: int, monitor_data: dict):
    db_monitor = session.get(Monitor, monitor_id)
    if not db_monitor:
        return None
    for key, value in monitor_data.items():
        setattr(db_monitor, key, value)
    session.add(db_monitor)
    session.commit()
    session.refresh(db_monitor)
    return db_monitor

def delete_monitor(session: Session, monitor_id: int):
    db_monitor = session.get(Monitor, monitor_id)
    if not db_monitor:
        return None
    session.delete(db_monitor)
    session.commit()
    return db_monitor