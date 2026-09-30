# main.py
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "A4 updated automatically testing successfully in c dir"}


@app.get("/health")
def health():
    return {"status": "ok"}
    
