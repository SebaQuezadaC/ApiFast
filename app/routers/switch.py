from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session
from app.crud.switch import create_switch, get_switch, update_switch, delete_switch
from app.schemas.switch import SwitchRead, SwitchCreate, SwitchUpdate
from app.models import Switch

router = APIRouter()

@router.post("/switch/", response_model=SwitchRead)
def create_new_switch(switch: SwitchCreate, session: Session = Depends(get_session)):
    db_switch = Switch.model_validate(switch)
    created_switch = create_switch(session, db_switch)
    return created_switch

@router.get("/switch/{switch_id}", response_model=SwitchRead)
def read_switch(switch_id: int, session: Session = Depends(get_session)):
    db_switch = get_switch(session, switch_id)
    if db_switch is None:
        raise HTTPException(status_code=404, detail="Switch not found")
    return db_switch

@router.put("/switch/{switch_id}", response_model=SwitchRead)
def update_switch(switch_id: int, switch: SwitchUpdate, session: Session = Depends(get_session)):
    db_switch = get_switch(session, switch_id)
    if db_switch is None:
        raise HTTPException(status_code=404, detail="Switch not found")
    
    switch_data = switch.model_dump(exclude_unset=True)
    for key, value in switch_data.items():
        setattr(db_switch, key, value)
    
    session.add(db_switch)
    session.commit()
    session.refresh(db_switch)
    return db_switch

@router.delete("/switch/{switch_id}", response_model=SwitchRead)
def delete_switch(switch_id: int, session: Session = Depends(get_session)):
    deleted_switch = delete_switch(session, switch_id)
    if deleted_switch is None:
        raise HTTPException(status_code=404, detail="Switch not found")
    return deleted_switch
