from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session
from app.crud.aire_comprimido import create_aire_comprimido, get_aire_comprimido, update_aire_comprimido, delete_aire_comprimido
from app.schemas.aire_comprimido import AireComprimidoRead, AireComprimidoCreate, AireComprimidoUpdate
from app.models import AireComprimido

router = APIRouter()

@router.post("/aire_comprimido/", response_model=AireComprimidoRead)
def create_new_aire_comprimido(aire_comprimido: AireComprimidoCreate, session: Session = Depends(get_session)):
    db_aire_comprimido = AireComprimido.model_validate(aire_comprimido)
    created_aire_comprimido = create_aire_comprimido(session, db_aire_comprimido)
    return created_aire_comprimido

@router.get("/aire_comprimido/{aire_comprimido_id}", response_model=AireComprimidoRead)
def read_aire_comprimido(aire_comprimido_id: int, session: Session = Depends(get_session)):
    db_aire_comprimido = get_aire_comprimido(session, aire_comprimido_id)
    if db_aire_comprimido is None:
        raise HTTPException(status_code=404, detail="Aire Comprimido not found")
    return db_aire_comprimido

@router.put("/aire_comprimido/{aire_comprimido_id}", response_model=AireComprimidoRead)
def update_aire_comprimido(aire_comprimido_id: int, aire_comprimido: AireComprimidoUpdate, session: Session = Depends(get_session)):
    db_aire_comprimido = get_aire_comprimido(session, aire_comprimido_id)
    if db_aire_comprimido is None:
        raise HTTPException(status_code=404, detail="Aire Comprimido not found")
    
    aire_comprimido_data = aire_comprimido.model_dump(exclude_unset=True)
    for key, value in aire_comprimido_data.items():
        setattr(db_aire_comprimido, key, value)
    
    session.add(db_aire_comprimido)
    session.commit()
    session.refresh(db_aire_comprimido)
    return db_aire_comprimido

@router.delete("/aire_comprimido/{aire_comprimido_id}", response_model=AireComprimidoRead)
def delete_aire_comprimido(aire_comprimido_id: int, session: Session = Depends(get_session)):
    deleted_aire_comprimido = delete_aire_comprimido(session, aire_comprimido_id)
    if deleted_aire_comprimido is None:
        raise HTTPException(status_code=404, detail="Aire Comprimido not found")
    return deleted_aire_comprimido
