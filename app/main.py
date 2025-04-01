from fastapi import FastAPI
from app.routers import home

app = FastAPI(title="FastAPI Docker Example")

# Include routers
app.include_router(home.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Dockerized App!"}
