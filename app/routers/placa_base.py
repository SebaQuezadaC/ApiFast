from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session
from app.crud.placa_base import create_placa_base, get_placa_base, update_placa_base, delete_placa_base
from app.schemas.placa_base import PlacaBaseRead, PlacaBaseCreate, PlacaBaseUpdate
from app.models import PlacaBase

router = APIRouter()

@router.post("/placa_base/", response_model=PlacaBaseRead)
def create_new_placa_base(placa_base: PlacaBaseCreate, session: Session = Depends(get_session)):
    db_placa_base = PlacaBase.model_validate(placa_base)
    created_placa_base = create_placa_base(session, db_placa_base)
    return created_placa_base

@router.get("/placa_base/{placa_base_id}", response_model=PlacaBaseRead)
def read_placa_base(placa_base_id: int, session: Session = Depends(get_session)):
    db_placa_base = get_placa_base(session, placa_base_id)
    if db_placa_base is None:
        raise HTTPException(status_code=404, detail="PlacaBase not found")
    return db_placa_base

@router.put("/placa_base/{placa_base_id}", response_model=PlacaBaseRead)
def update_placa_base(placa_base_id: int, placa_base: PlacaBaseUpdate, session: Session = Depends(get_session)):
    db_placa_base = get_placa_base(session, placa_base_id)
    if db_placa_base is None:
        raise HTTPException(status_code=404, detail="PlacaBase not found")
    
    placa_base_data = placa_base.model_dump(exclude_unset=True)
    for key, value in placa_base_data.items():
        setattr(db_placa_base, key, value)
    
    session.add(db_placa_base)
    session.commit()
    session.refresh(db_placa_base)
    return db_placa_base

@router.delete("/placa_base/{placa_base_id}", response_model=PlacaBaseRead)
def delete_placa_base(placa_base_id: int, session: Session = Depends(get_session)):
    deleted_placa_base = delete_placa_base(session, placa_base_id)
    if deleted_placa_base is None:
        raise HTTPException(status_code=404, detail="PlacaBase not found")
    return deleted_placa_base
