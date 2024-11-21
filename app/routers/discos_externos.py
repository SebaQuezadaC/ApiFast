from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session
from app.crud.discos_externos import create_discos_externos, get_discos_externos, update_discos_externos, delete_discos_externos
from app.schemas.discos_externos import DiscosExternosRead, DiscosExternosCreate, DiscosExternosUpdate
from app.models import DiscosExternos

router = APIRouter()

@router.post("/discos_externos/", response_model=DiscosExternosRead)
def create_new_discos_externos(discos_externos: DiscosExternosCreate, session: Session = Depends(get_session)):
    db_discos_externos = DiscosExternos.model_validate(discos_externos)
    created_discos_externos = create_discos_externos(session, db_discos_externos)
    return created_discos_externos

@router.get("/discos_externos/{discos_externos_id}", response_model=DiscosExternosRead)
def read_discos_externos(discos_externos_id: int, session: Session = Depends(get_session)):
    db_discos_externos = get_discos_externos(session, discos_externos_id)
    if db_discos_externos is None:
        raise HTTPException(status_code=404, detail="Discos Externos not found")
    return db_discos_externos

@router.put("/discos_externos/{discos_externos_id}", response_model=DiscosExternosRead)
def update_discos_externos(discos_externos_id: int, discos_externos: DiscosExternosUpdate, session: Session = Depends(get_session)):
    db_discos_externos = get_discos_externos(session, discos_externos_id)
    if db_discos_externos is None:
        raise HTTPException(status_code=404, detail="Discos Externos not found")
    
    discos_externos_data = discos_externos.model_dump(exclude_unset=True)
    for key, value in discos_externos_data.items():
        setattr(db_discos_externos, key, value)
    
    session.add(db_discos_externos)
    session.commit()
    session.refresh(db_discos_externos)
    return db_discos_externos

@router.delete("/discos_externos/{discos_externos_id}", response_model=DiscosExternosRead)
def delete_discos_externos(discos_externos_id: int, session: Session = Depends(get_session)):
    deleted_discos_externos = delete_discos_externos(session, discos_externos_id)
    if deleted_discos_externos is None:
        raise HTTPException(status_code=404, detail="Discos Externos not found")
    return deleted_discos_externos
