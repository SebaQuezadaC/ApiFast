from pydantic import BaseModel

class AdaptadorBase(BaseModel):
    marca: str
    modelo: str
    estado: str

class AdaptadorCreate(AdaptadorBase):
    pass

class AdaptadorRead(AdaptadorBase):
    id: int

class AdaptadorUpdate(BaseModel):
    marca: str | None = None
    modelo: str | None = None
    estado: str | None = None
