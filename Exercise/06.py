from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/news/{id}")
async def get_news_by_id(
        id: int = Path(..., ge=1, le=100, description="新闻分类ID，范围1~100")
):
    return {"news_id":id,"message":f"查询ID为{id}的新闻分类"}

@app.get("/news/{name}")
async def get_news_by_name(
        name:str = Path(..., min_length=2, max_length=10,description="新闻分类名称，长度2~10")
):
    return {"news_name":{name},"message":f"查询名称为{name}的新闻分类"}