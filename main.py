from fastapi import FastAPI, Request
from uvicorn import run

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Olá, mundo!"}