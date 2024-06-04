from routers.schemas import PostBase
from .models import DbPost
from sqlalchemy.orm.session import Session
from datetime import datetime
from fastapi import HTTPException,status


def create_post(request: PostBase,db: Session) -> DbPost:
    new_post = DbPost(image_url=request.image_url,
                      title=request.title,
                      content=request.content,
                      creator=request.creator,
                      timestamp=datetime.now()
                      )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all(db: Session):
    return db.query(DbPost).all()

def delete_post(db: Session, id: int):
    post = db.query(DbPost).filter(DbPost.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} not found.")
    db.delete(post)
    db.commit()
    return f"Post with id {id} deleted."