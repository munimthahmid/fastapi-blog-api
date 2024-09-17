from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from ..hashing import Hash
from datetime import timedelta
from ..token import create_access_token
from ..schemas import Token
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
router=APIRouter(
     
    tags=["Authentication"],
)
ACCESS_TOKEN_EXPIRE_MINUTES = 30

@router.post("/login")
def login(request:Annotated[OAuth2PasswordRequestForm, Depends()],db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    if not Hash.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


