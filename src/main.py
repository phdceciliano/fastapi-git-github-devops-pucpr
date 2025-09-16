from fastapi import FastAPI
from src.routers import alunos, treinos


# endpoints
# http://127.0.0.1:8000

app = FastAPI(title="Sistema Academia CRUD", version="1.0.0")

# Incluir routers
app.include_router(alunos.router, prefix="/alunos", tags=["alunos"])
app.include_router(treinos.router, prefix="/treinos", tags=["treinos"])

@app.get("/")
async def root():
    return {"message": "Sistema de Academia CRUD"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}