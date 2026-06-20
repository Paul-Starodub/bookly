from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class BookCreateModel(BaseModel):
    title: str
    author: str


@app.get("/")
async def read_root() -> dict:
    return {"message": "Hello World"}


# @app.get("/greet/{name}/")
# async def greet_name(name: str) -> dict:
#     return {"message": f"Hello {name}"}


# @app.get("/greet/")
# async def greet_name(name: str) -> dict:
#     return {"message": f"Hello {name}"}


# @app.get("/greet/{name}/")
# async def greet_name(name: str, age: int) -> dict:
#     return {"message": f"Hello {name}, age: {age}"}


@app.get("/greet/")
async def greet_name(age: int = 0, name: str | None = "User") -> dict:
    return {"message": f"Hello {name}, age: {age}"}


@app.post("/create_book/")
async def create_book(book_data: BookCreateModel) -> dict:
    return {"message": f"Book created: {book_data.title} by {book_data.author}"}
