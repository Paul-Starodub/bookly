from fastapi import FastAPI, Header
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


@app.get("/get_headers/")
async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None),
) -> dict:
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = host
    return request_headers
