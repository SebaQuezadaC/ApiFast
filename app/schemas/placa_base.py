from pydantic import BaseModel

class PlacaBaseBase(BaseModel):
    marca: str
    slots_memorias: str
    modelo: str
    sockets: str
    chipset: str
    formato: str

class PlacaBaseCreate(PlacaBaseBase):
    pass

class PlacaBaseRead(PlacaBaseBase):
    id: int

class PlacaBaseUpdate(BaseModel):
    marca: str | None = None
    slots_memorias: str | None = None
    modelo: str | None = None
    sockets: str | None = None
    chipset: str | None = None
    formato: str | None = None
