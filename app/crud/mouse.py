from sqlmodel import Session, select
from app.models import Mouse

def create_mouse(session: Session, mouse: Mouse):
    session.add(mouse)
    session.commit()
    session.refresh(mouse)
    return mouse

def get_mouse(session: Session, mouse_id: int):
    return session.get(Mouse, mouse_id)

def update_mouse(session: Session, mouse_id: int, mouse_data: dict):
    db_mouse = session.get(Mouse, mouse_id)
    if not db_mouse:
        return None
    for key, value in mouse_data.items():
        setattr(db_mouse, key, value)
    session.add(db_mouse)
    session.commit()
    session.refresh(db_mouse)
    return db_mouse

def delete_mouse(session: Session, mouse_id: int):
    db_mouse = session.get(Mouse, mouse_id)
    if not db_mouse:
        return None
    session.delete(db_mouse)
    session.commit()
    return db_mouse