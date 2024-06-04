from fastapi import FastAPI
from databases import models
from databases.database import engine
from routers import post

app = FastAPI()
app.include_router(post.router)


models.Base.metadata.create_all(engine)
