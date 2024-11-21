from pydantic import BaseModel

class AlcoholBase(BaseModel):
    cantidad: int

class AlcoholCreate(AlcoholBase):
    pass

class AlcoholRead(AlcoholBase):
    id: int

class AlcoholUpdate(BaseModel):
    cantidad: int | None = None
