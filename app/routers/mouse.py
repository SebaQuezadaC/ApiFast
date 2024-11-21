from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session
from app.crud.mouse import create_mouse, get_mouse, update_mouse, delete_mouse as crud_delete_mouse
from app.schemas.mouse import MouseRead, MouseCreate, MouseUpdate
from app.models import Mouse

router = APIRouter()

@router.post("/mouse/", response_model=MouseRead)
def create_new_mouse(mouse: MouseCreate, session: Session = Depends(get_session)):
    db_mouse = Mouse.model_validate(mouse)  # Convertir de mouseCreate a mouse usando model_validate
    created_mouse = create_mouse(session, db_mouse)
    return created_mouse

@router.get("/mouse/{mouse_id}", response_model=MouseRead)
def read_mouse(mouse_id: int, session: Session = Depends(get_session)):
    db_mouse = get_mouse(session, mouse_id)
    if db_mouse is None:
        raise HTTPException(status_code=404, detail="mouse not found")
    return db_mouse

@router.put("/mouse/{mouse_id}", response_model=MouseRead)
def update_mouse(mouse_id: int, mouse: MouseUpdate, session: Session = Depends(get_session)):
    db_mouse = get_mouse(session, mouse_id)
    if db_mouse is None:
        raise HTTPException(status_code=404, detail="mouse not found")
    
    # Usar model_dump en lugar de dict
    mouse_data = mouse.model_dump(exclude_unset=True)
    # Actualizar db_mouse con los valores de mouse_data
    for key, value in mouse_data.items():
        setattr(db_mouse, key, value)
    
    session.add(db_mouse)
    session.commit()
    session.refresh(db_mouse)
    return db_mouse

@router.delete("/mouse/{mouse_id}", response_model=MouseRead)
def delete_mouse(mouse_id: int, session: Session = Depends(get_session)):
    deleted_mouse = crud_delete_mouse(session, mouse_id)  # Llamar a la función correcta en crud.py
    if deleted_mouse is None:
        raise HTTPException(status_code=404, detail="mouse not found")
    return deleted_mouse
