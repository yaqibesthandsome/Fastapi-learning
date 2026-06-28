from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/book/book_list")
async def get_book_list(
        sort:str=Query("Python开发",min_length=5,max_length=255,description="图书分类，默认Python开发"),
        price:float=Query(...,ge=50,le=100,description="图书价格，范围50~100")
):
    return {"sort":sort,"price":price,"message":f"查询到种类为{sort},价格为{price}的图书"}