from fastapi import FastAPI, staticfiles
from fastapi.middleware.cors import CORSMiddleware
from databases import models
from databases.database import engine
from routers import post

app = FastAPI()
app.include_router(post.router)


models.Base.metadata.create_all(engine)

app.mount(path="/images",app=staticfiles.StaticFiles(directory="images"),name="images")

origins = [
    "http://localhost:3000"
]

app.add_middleware(CORSMiddleware,
                   allow_origins = origins,
                   allow_credentials = True,
                   allow_methods = ["*"],
                   allow_headers = ["*"]
                   )