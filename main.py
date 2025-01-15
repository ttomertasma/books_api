from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/books/{book_id}")
def git_book(book_id:int):
    return {"title": "tomer first book",
             "author": "levi",
             "date": "01/01/2025"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}