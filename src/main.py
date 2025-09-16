from fastapi import FastAPI
from src.routers import alunos, treinos

app = FastAPI(title="Sistema Academia CRUD", version="1.0.0")


# Incluir routers
app.include_router(alunos.router, prefix="/alunos", tags=["alunos"])
app.include_router(treinos.router, prefix="/treinos", tags=["treinos"])
# sistema

@app.get("/")
async def root():
    return {"message": "Sistema de Academia CRUD"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
