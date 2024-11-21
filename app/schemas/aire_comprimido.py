from pydantic import BaseModel

class AireComprimidoBase(BaseModel):
    cantidad: int

class AireComprimidoCreate(AireComprimidoBase):
    pass

class AireComprimidoRead(AireComprimidoBase):
    id: int

class AireComprimidoUpdate(BaseModel):
    cantidad: int | None = None
