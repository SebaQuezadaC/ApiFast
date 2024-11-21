from sqlmodel import SQLModel, Field
from typing import Optional

class Ram(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    capacidad: int
    tipo: str
    frecuencia: str
    marca: str
    estado: str


class Notebook(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    marca: str
    modelo: str
    procesador: str
    tipo_ram: str
    capacidad_ram: int
    almacenamiento_principal: str
    almacenamiento_principal_capacidad: int
    almacenamiento_secundario: Optional[str] = Field(default=None)
    almacenamiento_secundario_capacidad: Optional[int] = Field(default=None)
    tarjeta_video: str
    estado_notebook: str
    cargador_disponible: str
    estado_bateria: str

class Monitor(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    marca: str
    modelo: str
    tamaño: str
    cargador: str
    estado: str

class Mouse(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    marca: str
    modelo: str
    estado: str
    cableado: str

class Microfono(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    marca: str
    modelo: str
    estado: str
    cableado: str

class Alcohol(SQLModel, table=True):
    id: int = Field(primary_key=True)
    cantidad: int

class AireComprimido(SQLModel, table=True):
    id: int = Field(primary_key=True)
    cantidad: int

class Switch(SQLModel, table=True):
    id: int = Field(primary_key=True)
    marca: str
    modelo: str
    estado: str

class Refrigeracion(SQLModel, table=True):
    id: int = Field(primary_key=True)
    marca: str
    modelo: str
    sockets: str
    tipo: str

class PlacaBase(SQLModel, table=True):
    id: int = Field(primary_key=True)
    marca: str
    slots_memorias: str
    modelo: str
    sockets: str
    chipset: str
    formato: str

class Teclado(SQLModel, table=True):
    id: int = Field(primary_key=True)
    marca: str
    modelo: str
    cableado: str
    estado: str

class Adaptador(SQLModel, table=True):
    id: int = Field(primary_key=True)
    marca: str
    modelo: str
    estado: str

class DiscosExternos(SQLModel, table=True):
    id: int = Field(primary_key=True)
    marca: str
    modelo: str
    capacidad: str
    estado: str
