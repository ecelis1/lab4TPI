from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from routers.jwt_man import token_router
from routers.usuarios import usuarios_router
from routers.categorias import Categoria_router
from routers.inscripciones import inscripciones_router
from routers.eventos import eventos_router

app = FastAPI()
app.title = "SISTEMA DE GESTIÓN DE EVENTOS"
app.version = "0.0.1"

app.include_router(token_router)
app.include_router(usuarios_router)
app.include_router(Categoria_router)
app.include_router(inscripciones_router)
app.include_router(eventos_router)

Base.metadata.create_all(bind=engine)

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>SISTEMA DE GESTIÓN DE EVENTOS</h1>')
