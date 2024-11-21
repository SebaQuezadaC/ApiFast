from pydantic import BaseModel

class DiscosExternosBase(BaseModel):
    marca: str
    modelo: str
    capacidad: str
    estado: str

class DiscosExternosCreate(DiscosExternosBase):
    pass

class DiscosExternosRead(DiscosExternosBase):
    id: int

class DiscosExternosUpdate(BaseModel):
    marca: str | None = None
    modelo: str | None = None
    capacidad: str | None = None
    estado: str | None = None
