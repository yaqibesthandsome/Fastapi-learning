from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    book_name:str
    zuozhe:str
    chubanse:str
    price:float

@app.post("/book")
async def add_book(book:Book):
    return {"message":"成功添加图书","book":book}