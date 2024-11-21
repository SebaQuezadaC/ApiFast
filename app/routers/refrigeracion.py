from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session
from app.crud.refrigeracion import create_refrigeracion, get_refrigeracion, update_refrigeracion, delete_refrigeracion
from app.schemas.refrigeracion import RefrigeracionRead, RefrigeracionCreate, RefrigeracionUpdate
from app.models import Refrigeracion

router = APIRouter()

@router.post("/refrigeracion/", response_model=RefrigeracionRead)
def create_new_refrigeracion(refrigeracion: RefrigeracionCreate, session: Session = Depends(get_session)):
    db_refrigeracion = Refrigeracion.model_validate(refrigeracion)
    created_refrigeracion = create_refrigeracion(session, db_refrigeracion)
    return created_refrigeracion

@router.get("/refrigeracion/{refrigeracion_id}", response_model=RefrigeracionRead)
def read_refrigeracion(refrigeracion_id: int, session: Session = Depends(get_session)):
    db_refrigeracion = get_refrigeracion(session, refrigeracion_id)
    if db_refrigeracion is None:
        raise HTTPException(status_code=404, detail="Refrigeracion not found")
    return db_refrigeracion

@router.put("/refrigeracion/{refrigeracion_id}", response_model=RefrigeracionRead)
def update_refrigeracion(refrigeracion_id: int, refrigeracion: RefrigeracionUpdate, session: Session = Depends(get_session)):
    db_refrigeracion = get_refrigeracion(session, refrigeracion_id)
    if db_refrigeracion is None:
        raise HTTPException(status_code=404, detail="Refrigeracion not found")
    
    refrigeracion_data = refrigeracion.model_dump(exclude_unset=True)
    for key, value in refrigeracion_data.items():
        setattr(db_refrigeracion, key, value)
    
    session.add(db_refrigeracion)
    session.commit()
    session.refresh(db_refrigeracion)
    return db_refrigeracion

@router.delete("/refrigeracion/{refrigeracion_id}", response_model=RefrigeracionRead)
def delete_refrigeracion(refrigeracion_id: int, session: Session = Depends(get_session)):
    deleted_refrigeracion = delete_refrigeracion(session, refrigeracion_id)
    if deleted_refrigeracion is None:
        raise HTTPException(status_code=404, detail="Refrigeracion not found")
    return deleted_refrigeracion
