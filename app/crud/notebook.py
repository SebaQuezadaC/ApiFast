from sqlmodel import Session, select
from app.models import Notebook


def create_notebook(session: Session, notebook: Notebook):
    session.add(notebook)
    session.commit()
    session.refresh(notebook)
    return notebook

def get_notebook(session: Session, notebook_id: int):
    return session.get(Notebook, notebook_id)

def update_notebook(session: Session, notebook_id: int, notebook_data: dict):
    db_notebook = session.get(Notebook, notebook_id)
    if not db_notebook:
        return None
    for key, value in notebook_data.items():
        setattr(db_notebook, key, value)
    session.add(db_notebook)
    session.commit()
    session.refresh(db_notebook)
    return db_notebook

def delete_notebook(session: Session, notebook_id: int):
    db_notebook = session.get(Notebook, notebook_id)
    if not db_notebook:
        return None
    session.delete(db_notebook)
    session.commit()
    return db_notebook
