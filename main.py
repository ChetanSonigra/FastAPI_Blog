from fastapi import FastAPI
from databases import models
from databases.database import engine

app = FastAPI()

@app.get("/")
def hw():
    return "Hello World"


models.Base.metadata.create_all(engine)
