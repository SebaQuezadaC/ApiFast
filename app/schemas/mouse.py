from pydantic import BaseModel

class MouseBase(BaseModel):
    marca: str
    modelo: str
    estado: str
    cableado: str

class MouseCreate(MouseBase):
    pass

class MouseRead(MouseBase):
    id: int

class MouseUpdate(BaseModel):
    marca: str | None = None
    modelo: str | None = None
    estado: str | None = None
    cableado: str | None = None
