from fastapi import FastAPI, staticfiles
from databases import models
from databases.database import engine
from routers import post

app = FastAPI()
app.include_router(post.router)


models.Base.metadata.create_all(engine)

app.mount(path="/images",app=staticfiles.StaticFiles(directory="images"),name="images")
