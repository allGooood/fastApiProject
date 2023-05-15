from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from DTO.post_test import PostTestRequestDTO
from setting import config
from database import get_db
from entity import TestEntity

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str, db: Session = Depends(get_db)):
    testEntity = db.query(TestEntity).first()
    return {"message": f"Hello {name}"}


@app.get("/test")
async def get_test(name: str):
    return {"message": f"Test {name}"}


@app.post("/test")
async def get_test(post_test_request: PostTestRequestDTO):
    return {"message": f"Test {post_test_request.name}"}
