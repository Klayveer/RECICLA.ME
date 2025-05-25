from fastapi import FastAPI
from . import models, database
from .routers import atendimento, usuarios, loja, servicos, blog, contato

app = FastAPI(title="API - Núcleo AMADO")

models.Base.metadata.create_all(bind=database.engine)

app.include_router(atendimento.router)
app.include_router(usuarios.router)
app.include_router(loja.router)
app.include_router(servicos.router)
app.include_router(blog.router)
app.include_router(contato.router)