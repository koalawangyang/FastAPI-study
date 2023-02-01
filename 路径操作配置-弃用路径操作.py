# 路径操作配置-弃用路径操作 deprecated

from fastapi import FastAPI

app = FastAPI()


@app.get("/users/", deprecated=True)
async def read_users():
    return "a blank users list"


@app.get("/items/", deprecated=False)
async def read_items():
    return "a blank items list"