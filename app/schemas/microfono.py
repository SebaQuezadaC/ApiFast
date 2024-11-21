from pydantic import BaseModel

class MicrofonoBase(BaseModel):
    marca: str
    modelo: str
    estado: str
    cableado: str

class MicrofonoCreate(MicrofonoBase):
    pass

class MicrofonoRead(MicrofonoBase):
    id: int

class MicrofonoUpdate(BaseModel):
    marca: str | None = None
    modelo: str | None = None
    estado: str | None = None
    cableado: str | None = None