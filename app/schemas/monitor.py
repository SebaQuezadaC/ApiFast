from pydantic import BaseModel

class MonitorBase(BaseModel):
    marca: str
    modelo: str
    tamaño: str
    cargador: str
    estado: str

class MonitorCreate(MonitorBase):
    pass

class MonitorRead(MonitorBase):
    id: int

class MonitorUpdate(BaseModel):
    marca: str | None = None
    modelo: str | None = None
    tamaño: str | None = None
    cargador: str | None = None
    estado: str | None = None