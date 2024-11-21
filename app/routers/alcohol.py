from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session
from app.crud.alcohol import create_alcohol, get_alcohol, update_alcohol, delete_alcohol
from app.schemas.alcohol import AlcoholRead, AlcoholCreate, AlcoholUpdate
from app.models import Alcohol

router = APIRouter()

@router.post("/alcohol/", response_model=AlcoholRead)
def create_new_alcohol(alcohol: AlcoholCreate, session: Session = Depends(get_session)):
    db_alcohol = Alcohol.model_validate(alcohol)
    created_alcohol = create_alcohol(session, db_alcohol)
    return created_alcohol

@router.get("/alcohol/{alcohol_id}", response_model=AlcoholRead)
def read_alcohol(alcohol_id: int, session: Session = Depends(get_session)):
    db_alcohol = get_alcohol(session, alcohol_id)
    if db_alcohol is None:
        raise HTTPException(status_code=404, detail="Alcohol not found")
    return db_alcohol

@router.put("/alcohol/{alcohol_id}", response_model=AlcoholRead)
def update_alcohol(alcohol_id: int, alcohol: AlcoholUpdate, session: Session = Depends(get_session)):
    db_alcohol = get_alcohol(session, alcohol_id)
    if db_alcohol is None:
        raise HTTPException(status_code=404, detail="Alcohol not found")
    
    alcohol_data = alcohol.model_dump(exclude_unset=True)
    for key, value in alcohol_data.items():
        setattr(db_alcohol, key, value)
    
    session.add(db_alcohol)
    session.commit()
    session.refresh(db_alcohol)
    return db_alcohol

@router.delete("/alcohol/{alcohol_id}", response_model=AlcoholRead)
def delete_alcohol(alcohol_id: int, session: Session = Depends(get_session)):
    deleted_alcohol = delete_alcohol(session, alcohol_id)
    if deleted_alcohol is None:
        raise HTTPException(status_code=404, detail="Alcohol not found")
    return deleted_alcohol
