from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session
from app.crud.ram import create_ram, get_ram, update_ram, delete_ram as crud_delete_ram
from app.schemas.ram import RAMCreate, RAMRead, RAMUpdate
from app.models import Ram

router = APIRouter()

@router.post("/ram/", response_model=RAMRead)
def create_new_ram(ram: RAMCreate, session: Session = Depends(get_session)):
    db_ram = Ram.model_validate(ram)  # Convertir de RAMCreate a RAM usando model_validate
    created_ram = create_ram(session, db_ram)
    return created_ram

@router.get("/ram/{ram_id}", response_model=RAMRead)
def read_ram(ram_id: int, session: Session = Depends(get_session)):
    db_ram = get_ram(session, ram_id)
    if db_ram is None:
        raise HTTPException(status_code=404, detail="RAM not found")
    return db_ram

@router.put("/ram/{ram_id}", response_model=RAMRead)
def update_ram(ram_id: int, ram: RAMUpdate, session: Session = Depends(get_session)):
    db_ram = get_ram(session, ram_id)
    if db_ram is None:
        raise HTTPException(status_code=404, detail="RAM not found")
    
    # Usar model_dump en lugar de dict
    ram_data = ram.model_dump(exclude_unset=True)
    # Actualizar db_ram con los valores de ram_data
    for key, value in ram_data.items():
        setattr(db_ram, key, value)
    
    session.add(db_ram)
    session.commit()
    session.refresh(db_ram)
    return db_ram


@router.delete("/ram/{ram_id}", response_model=RAMRead)
def delete_ram(ram_id: int, session: Session = Depends(get_session)):
    deleted_ram = crud_delete_ram(session, ram_id)  # Llamar a la función correcta en crud.py
    if deleted_ram is None:
        raise HTTPException(status_code=404, detail="RAM not found")
    return deleted_ram
