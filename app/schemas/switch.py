from pydantic import BaseModel

class SwitchBase(BaseModel):
    marca: str
    modelo: str
    estado: str

class SwitchCreate(SwitchBase):
    pass

class SwitchRead(SwitchBase):
    id: int

class SwitchUpdate(BaseModel):
    marca: str | None = None
    modelo: str | None = None
    estado: str | None = None
