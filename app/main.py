from fastapi import FastAPI
from app.blog import models
from app.blog.database import engine
models.Base.metadata.create_all(bind=engine)
from app.blog.routers import blog, users,authentication
app=FastAPI()

models.Base.metadata.create_all(engine)
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(users.router)

