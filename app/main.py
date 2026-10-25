from fastapi import FastAPI

app = FastAPI(title="Public Data API")


@app.get("/")
def root():
    return {"message": "Public Data API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}