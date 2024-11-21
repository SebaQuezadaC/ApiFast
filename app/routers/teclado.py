from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session
from app.crud.teclado import create_teclado, get_teclado, update_teclado, delete_teclado
from app.schemas.teclado import TecladoRead, TecladoCreate, TecladoUpdate
from app.models import Teclado

router = APIRouter()

@router.post("/teclado/", response_model=TecladoRead)
def create_new_teclado(teclado: TecladoCreate, session: Session = Depends(get_session)):
    db_teclado = Teclado.model_validate(teclado)
    created_teclado = create_teclado(session, db_teclado)
    return created_teclado

@router.get("/teclado/{teclado_id}", response_model=TecladoRead)
def read_teclado(teclado_id: int, session: Session = Depends(get_session)):
    db_teclado = get_teclado(session, teclado_id)
    if db_teclado is None:
        raise HTTPException(status_code=404, detail="Teclado not found")
    return db_teclado

@router.put("/teclado/{teclado_id}", response_model=TecladoRead)
def update_teclado(teclado_id: int, teclado: TecladoUpdate, session: Session = Depends(get_session)):
    db_teclado = get_teclado(session, teclado_id)
    if db_teclado is None:
        raise HTTPException(status_code=404, detail="Teclado not found")
    
    teclado_data = teclado.model_dump(exclude_unset=True)
    for key, value in teclado_data.items():
        setattr(db_teclado, key, value)
    
    session.add(db_teclado)
    session.commit()
    session.refresh(db_teclado)
    return db_teclado

@router.delete("/teclado/{teclado_id}", response_model=TecladoRead)
def delete_teclado(teclado_id: int, session: Session = Depends(get_session)):
    deleted_teclado = delete_teclado(session, teclado_id)
    if deleted_teclado is None:
        raise HTTPException(status_code=404, detail="Teclado not found")
    return deleted_teclado
