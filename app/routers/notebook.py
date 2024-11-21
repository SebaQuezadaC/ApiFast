from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session
from app.crud.notebook import create_notebook, get_notebook, update_notebook, delete_notebook as crud_delete_notebook
from app.schemas.notebook import NotebookCreate, NotebookRead, NotebookUpdate
from app.models import Notebook

router = APIRouter()

@router.post("/notebook/", response_model=NotebookRead)
def create_new_notebook(notebook: NotebookCreate, session: Session = Depends(get_session)):
    db_notebook = Notebook.model_validate(notebook)  # Convertir de notebookCreate a notebook usando model_validate
    created_notebook = create_notebook(session, db_notebook)
    return created_notebook

@router.get("/notebook/{notebook_id}", response_model=NotebookRead)
def read_notebook(notebook_id: int, session: Session = Depends(get_session)):
    db_notebook = get_notebook(session, notebook_id)
    if db_notebook is None:
        raise HTTPException(status_code=404, detail="notebook not found")
    return db_notebook

@router.put("/notebook/{notebook_id}", response_model=NotebookRead)
def update_notebook(notebook_id: int, notebook: NotebookUpdate, session: Session = Depends(get_session)):
    db_notebook = get_notebook(session, notebook_id)
    if db_notebook is None:
        raise HTTPException(status_code=404, detail="Notebook not found")
    
    # Usar model_dump en lugar de dict
    notebook_data = notebook.model_dump(exclude_unset=True)
    # Actualizar db_notebook con los valores de notebook_data
    for key, value in notebook_data.items():
        setattr(db_notebook, key, value)
    
    session.add(db_notebook)
    session.commit()
    session.refresh(db_notebook)
    return db_notebook


@router.delete("/notebook/{notebook_id}", response_model=NotebookRead)
def delete_notebook(notebook_id: int, session: Session = Depends(get_session)):
    deleted_notebook = crud_delete_notebook(session, notebook_id)  # Llamar a la función correcta en crud.py
    if deleted_notebook is None:
        raise HTTPException(status_code=404, detail="notebook not found")
    return deleted_notebook
