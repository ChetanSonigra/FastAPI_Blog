from fastapi import APIRouter,Depends
from databases.database import get_db
from databases import db_post
from sqlalchemy.orm.session import Session
from routers.schemas import PostBase,PostDisplay

router = APIRouter(prefix="/post",
                   tags=["post"]
                )

@router.post("")
def create_post(request:PostBase,db: Session = Depends(get_db)):
    return db_post.create_post(request,db)
    