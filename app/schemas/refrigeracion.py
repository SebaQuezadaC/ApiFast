from pydantic import BaseModel

class RefrigeracionBase(BaseModel):
    marca: str
    modelo: str
    sockets: str
    tipo: str

class RefrigeracionCreate(RefrigeracionBase):
    pass

class RefrigeracionRead(RefrigeracionBase):
    id: int

class RefrigeracionUpdate(BaseModel):
    marca: str | None = None
    modelo: str | None = None
    sockets: str | None = None
    tipo: str | None = None
