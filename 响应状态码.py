# 响应状态码

from fastapi import FastAPI, status


app = FastAPI()


@app.get("/", status_code=201)
async def root_page():
    return "Hello 201!"


# 可以使用 fastapi.status 的便捷变量，比如 201
@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}