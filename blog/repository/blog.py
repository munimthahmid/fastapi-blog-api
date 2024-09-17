from sqlalchemy.orm import Session
from .. import models
from .. import schemas
from fastapi import status,HTTPException

def get_all(db: Session):
     blogs = db.query(models.Blog).all()
     return blogs

def create(db:Session ,request:schemas.Blog):
    newBlog=models.Blog(title=request.title,body=request.body,creator_id=1)
    db.add(newBlog)
    db.commit()
    db.refresh(newBlog)
    return newBlog

def delete(db:Session,id:int):
    db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    db.commit()
    return f"Blog with id {id} was deleted successfully "

def update(id:int, request:schemas.Blog,db:Session):
    db.query(models.Blog).filter(models.Blog.id == id).update(request.model_dump())

    # Check if the blog exists

    # Commit the changes to the database
    db.commit()
    
    return {"message": "Update successful"}

def show(id:int, db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id {id} not found" )
    return blog
