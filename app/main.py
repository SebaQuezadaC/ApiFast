from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routers import ram, notebook, monitor, mouse, microfono, alcohol, aire_comprimido, switch, refrigeracion, placa_base, teclado, adaptador, discos_externos
from app.database import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Inicialización de recursos
    create_db_and_tables()  # Creación de tablas de la base de datos
    yield

    print("Aplicación cerrándose")

app = FastAPI(lifespan=lifespan)

app.include_router(ram.router)
app.include_router(notebook.router)
app.include_router(monitor.router)
app.include_router(mouse.router)
app.include_router(microfono.router)
app.include_router(alcohol.router)
app.include_router(aire_comprimido.router)
app.include_router(switch.router)
app.include_router(refrigeracion.router)
app.include_router(placa_base.router)
app.include_router(teclado.router)
app.include_router(adaptador.router)
app.include_router(discos_externos.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
