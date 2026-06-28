from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Worldlyq"}

@app.get("/hello")
async def get_hello():
    return {"msg":"你好,FastAPI"}