from fastapi import APIRouter,Depends, UploadFile, File
from databases.database import get_db
from databases import db_post
from sqlalchemy.orm.session import Session
from routers.schemas import PostBase,PostDisplay
import string, random, shutil

router = APIRouter(prefix="/post",
                   tags=["post"]
                )

@router.post("",response_model=PostDisplay)
def create_post(request:PostBase,db: Session = Depends(get_db)):
    return db_post.create_post(request,db)
    

@router.get("/all",response_model=list[PostDisplay])
def get_posts(db: Session = Depends(get_db)):
    return db_post.get_all(db)


@router.delete("/delete")
def delete_post(id: int, db: Session = Depends(get_db)):
    return db_post.delete_post(db,id)


@router.post("/image")
def upload_image(image: UploadFile = File(...)):
    letters = string.ascii_letters
    rand_str = "".join(random.choice(letters) for i in range(6))
    new = f"_{rand_str}."
    filename = new.join(image.filename.rsplit(".",1))
    path = f"images/{filename}"

    with open(path,"w+b") as buffer:
        shutil.copyfileobj(image.file,buffer)

    return {
        "filename": path
    }