from routers.schemas import PostBase
from .models import DbPost
from sqlalchemy.orm.session import Session
from datetime import datetime


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
