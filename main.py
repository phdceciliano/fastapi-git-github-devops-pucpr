import random

from fastapi import FastAPI

app = FastAPI()

# endpoints 
# http://127.0.0.1:8000
@app.get("/")
async def root():
    return {"message": "API - HelloWorld"}
# http://127.0.0.1:8000/testando
@app.get("/teste1")
async def funcaoteste():
    return {"teste":True, "num_aleatorio": random.randint(0, 1000)}