from pydantic import BaseModel

class TecladoBase(BaseModel):
    marca: str
    modelo: str
    cableado: str
    estado: str

class TecladoCreate(TecladoBase):
    pass

class TecladoRead(TecladoBase):
    id: int

class TecladoUpdate(BaseModel):
    marca: str | None = None
    modelo: str | None = None
    cableado: str | None = None
    estado: str | None = None
