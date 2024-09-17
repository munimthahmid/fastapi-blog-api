from fastapi import APIRouter,Depends
from fastapi import FastAPI, Depends, status,HTTPException
from ..database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List
import databases
from .. import schemas
from .. import models  # Make sure to import models
from ..repository import blog
from typing import Annotated
from ..schemas import User
from ..oath2 import get_current_user
router=APIRouter(

    tags=["Blogs"],
    prefix="/blog"
)
def row_to_dict(row, keys):
    keys = list(keys)  # Convert keys to a list
    return {keys[i]: row[i] for i in range(len(keys))}

@router.get("/", response_model=List[schemas.ShowBlog])
def get_all_blogs( current_user: Annotated[User, Depends(get_current_user)],db: Session = Depends(get_db),):
    return blog.get_all(db)
   

@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schemas.ShowBlog)
def create(current_user: Annotated[User, Depends(get_current_user)],request: schemas.Blog, db:Session=Depends(get_db)):
    return blog.create(db,request)

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete(current_user: Annotated[User, Depends(get_current_user)],id,db:Session=Depends(get_db) ):
   return blog.delete(db,id)




@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(current_user: Annotated[User, Depends(get_current_user)],id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id,request,db)

@router.get("/{id}")
def show(current_user: Annotated[User, Depends(get_current_user)],id, db:Session=Depends(get_db)):
   return blog.show(id,db)