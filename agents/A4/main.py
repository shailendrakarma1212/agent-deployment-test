# main.py
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "A4 running"}


@app.get("/health")
def health():
    return {"status": "ok"}
