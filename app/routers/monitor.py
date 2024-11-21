from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session
from app.crud.monitor import create_monitor, get_monitor, update_monitor, delete_monitor as crud_delete_monitor
from app.schemas.monitor import MonitorRead, MonitorCreate, MonitorUpdate
from app.models import Monitor

router = APIRouter()

@router.post("/monitor/", response_model=MonitorRead)
def create_new_monitor(monitor: MonitorCreate, session: Session = Depends(get_session)):
    db_monitor = Monitor.model_validate(monitor)  # Convertir de MonitorCreate a monitor usando model_validate
    created_monitor = create_monitor(session, db_monitor)
    return created_monitor

@router.get("/monitor/{monitor_id}", response_model=MonitorRead)
def read_monitor(monitor_id: int, session: Session = Depends(get_session)):
    db_monitor = get_monitor(session, monitor_id)
    if db_monitor is None:
        raise HTTPException(status_code=404, detail="monitor not found")
    return db_monitor

@router.put("/monitor/{monitor_id}", response_model=MonitorRead)
def update_monitor(monitor_id: int, monitor: MonitorUpdate, session: Session = Depends(get_session)):
    db_monitor = get_monitor(session, monitor_id)
    if db_monitor is None:
        raise HTTPException(status_code=404, detail="Monitor not found")
    
    # Usar model_dump en lugar de dict
    monitor_data = monitor.model_dump(exclude_unset=True)
    # Actualizar db_monitor con los valores de monitor_data
    for key, value in monitor_data.items():
        setattr(db_monitor, key, value)
    
    session.add(db_monitor)
    session.commit()
    session.refresh(db_monitor)
    return db_monitor

@router.delete("/monitor/{monitor_id}", response_model=MonitorRead)
def delete_monitor(monitor_id: int, session: Session = Depends(get_session)):
    deleted_monitor = crud_delete_monitor(session, monitor_id)  # Llamar a la función correcta en crud.py
    if deleted_monitor is None:
        raise HTTPException(status_code=404, detail="monitor not found")
    return deleted_monitor
