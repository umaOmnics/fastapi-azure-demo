from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message" : "Hello from Azure + Github actions"}

@app.get("/health")
def health():
    return {"status" : "ok"}