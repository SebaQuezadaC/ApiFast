from pydantic import BaseModel
from typing import Optional

class NotebookBase(BaseModel):
    marca: str
    modelo: str
    procesador: str
    tipo_ram: str
    capacidad_ram: int
    almacenamiento_principal: str
    almacenamiento_principal_capacidad: int
    almacenamiento_secundario: Optional[str] = None
    almacenamiento_secundario_capacidad: Optional[int] = None
    tarjeta_video: str
    estado_notebook: str
    cargador_disponible: str
    estado_bateria: str

class NotebookCreate(NotebookBase):
    pass

class NotebookRead(NotebookBase):
    id: int

class NotebookUpdate(BaseModel):
    marca: Optional[str] = None
    modelo: Optional[str] = None
    procesador: Optional[str] = None
    tipo_ram: Optional[str] = None
    capacidad_ram: Optional[int] = None
    almacenamiento_principal: Optional[str] = None
    almacenamiento_principal_capacidad: Optional[int] = None
    almacenamiento_secundario: Optional[str] = None
    almacenamiento_secundario_capacidad: Optional[int] = None
    tarjeta_video: Optional[str] = None
    estado_notebook: Optional[str] = None
    cargador_disponible: Optional[str] = None
    estado_bateria: Optional[str] = None
