from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app=FastAPI()



class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]=None

@app.get("/blog")
def index(limit:int =10, published:bool=True, sort:Optional[str]=None):
    return {f"List of blogs with limit {limit} and published {published}"}


@app.get("/about")
def about():
    return {"About":"This is a about page"}

@app.get("/blog/unpublished")
def unpublished():
    return {"List of Unpublished Blgos":"Yeah, None!"}

@app.get("/blog/{id}")
def blog(id:int):
    return {"Id of the blog":id}

@app.get("/blog/{id}/comments")
def comments(id):
    return {"Comments":{"1","2",3}}


@app.post("/blog")
def create_blog(blog: Blog):
    return {f"Blog is created with {blog.title}"}