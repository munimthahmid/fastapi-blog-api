from fastapi import APIRouter,Depends
from fastapi import FastAPI, Depends, status,HTTPException
from ..database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from sqlalchemy import text
from .. import schemas
from ..hashing import Hash
from .. import models  # Make sure to import models
from ..repository import user
router=APIRouter(
     
      tags=["Users"],
    prefix="/user"
)

@router.post("/", response_model=schemas.ShowUser, tags=["Users"])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    # Create a new user with correct keyword arguments
   return user.create_user(request,db)

@router.post("/{id}", response_model=schemas.ShowUser, tags=["Users"])
def get_user(id:int, db: Session = Depends(get_db)):
    return user.get_user(id,db)