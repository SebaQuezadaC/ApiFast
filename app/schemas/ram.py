from pydantic import BaseModel


class RAMBase(BaseModel):
    capacidad: int
    tipo: str
    frecuencia: str
    marca: str
    estado: str


class RAMCreate(RAMBase):
    pass

class RAMRead(RAMBase):
    id: int

class RAMUpdate(BaseModel):
    capacidad: int | None = None
    tipo: str | None = None
    frecuencia: str | None = None
    marca: str | None = None
    estado: str | None = None