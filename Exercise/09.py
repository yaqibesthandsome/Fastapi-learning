from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI()

class Book(BaseModel):
    book_name:str=Field(...,min_length=2,max_length=20,description="书名，长度2~20")
    zuozhe:str=Field(...,min_length=2,max_length=10,description="作者名，长度2~10")
    chubanse:str=Field(default="黑马出版社",description="出版社名，默认黑马出版社")
    price:float=Field(...,gt=0,description="价格大于0元")

@app.post("/book")
async def add_book(book:Book):
    return {"message":"成功添加图书","book":book}