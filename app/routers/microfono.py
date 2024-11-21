from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session
from app.crud.microfono import create_microfono, get_microfono, update_microfono, delete_microfono as crud_delete_microfono
from app.schemas.microfono import MicrofonoRead, MicrofonoCreate, MicrofonoUpdate
from app.models import Microfono

router = APIRouter()

@router.post("/microfono/", response_model=MicrofonoRead)
def create_new_microfono(microfono: MicrofonoCreate, session: Session = Depends(get_session)):
    db_microfono = Microfono.model_validate(microfono)  # Convertir de MicrofonoCreate a microfono usando model_validate
    created_microfono = create_microfono(session, db_microfono)
    return created_microfono

@router.get("/microfono/{microfono_id}", response_model=MicrofonoRead)
def read_microfono(microfono_id: int, session: Session = Depends(get_session)):
    db_microfono = get_microfono(session, microfono_id)
    if db_microfono is None:
        raise HTTPException(status_code=404, detail="microfono not found")
    return db_microfono

@router.put("/microfono/{microfono_id}", response_model=MicrofonoRead)
def update_microfono(microfono_id: int, microfono: MicrofonoUpdate, session: Session = Depends(get_session)):
    db_microfono = get_microfono(session, microfono_id)
    if db_microfono is None:
        raise HTTPException(status_code=404, detail="microfono not found")
    
    # Usar model_dump en lugar de dict
    microfono_data = microfono.model_dump(exclude_unset=True)
    # Actualizar db_microfono con los valores de microfono_data
    for key, value in microfono_data.items():
        setattr(db_microfono, key, value)
    
    session.add(db_microfono)
    session.commit()
    session.refresh(db_microfono)
    return db_microfono

@router.delete("/microfono/{microfono_id}", response_model=MicrofonoRead)
def delete_microfono(microfono_id: int, session: Session = Depends(get_session)):
    deleted_microfono = crud_delete_microfono(session, microfono_id)  # Llamar a la función correcta en crud.py
    if deleted_microfono is None:
        raise HTTPException(status_code=404, detail="microfono not found")
    return deleted_microfono
