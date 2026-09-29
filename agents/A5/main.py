from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "A5 running successfully service automatically deploye changes with testing "} 


@app.get("/health")
def health():
    return {"status": "ok", "agent": "A5"}
