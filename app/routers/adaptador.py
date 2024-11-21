from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session
from app.crud.adaptador import create_adaptador, get_adaptador, update_adaptador, delete_adaptador
from app.schemas.adaptador import AdaptadorRead, AdaptadorCreate, AdaptadorUpdate
from app.models import Adaptador

router = APIRouter()

@router.post("/adaptador/", response_model=AdaptadorRead)
def create_new_adaptador(adaptador: AdaptadorCreate, session: Session = Depends(get_session)):
    db_adaptador = Adaptador.model_validate(adaptador)
    created_adaptador = create_adaptador(session, db_adaptador)
    return created_adaptador

@router.get("/adaptador/{adaptador_id}", response_model=AdaptadorRead)
def read_adaptador(adaptador_id: int, session: Session = Depends(get_session)):
    db_adaptador = get_adaptador(session, adaptador_id)
    if db_adaptador is None:
        raise HTTPException(status_code=404, detail="Adaptador not found")
    return db_adaptador

@router.put("/adaptador/{adaptador_id}", response_model=AdaptadorRead)
def update_adaptador(adaptador_id: int, adaptador: AdaptadorUpdate, session: Session = Depends(get_session)):
    db_adaptador = get_adaptador(session, adaptador_id)
    if db_adaptador is None:
        raise HTTPException(status_code=404, detail="Adaptador not found")
    
    adaptador_data = adaptador.model_dump(exclude_unset=True)
    for key, value in adaptador_data.items():
        setattr(db_adaptador, key, value)
    
    session.add(db_adaptador)
    session.commit()
    session.refresh(db_adaptador)
    return db_adaptador

@router.delete("/adaptador/{adaptador_id}", response_model=AdaptadorRead)
def delete_adaptador(adaptador_id: int, session: Session = Depends(get_session)):
    deleted_adaptador = delete_adaptador(session, adaptador_id)
    if deleted_adaptador is None:
        raise HTTPException(status_code=404, detail="Adaptador not found")
    return deleted_adaptador
