# 依赖项-第一步
# 依赖项就是一个函数，且可以使用与路径操作函数相同的参数

from typing import Union
from fastapi import FastAPI, Depends

app = FastAPI()


async def common_parameters(
        q: Union[str, None] = None,
        skip: int = 0,
        limit: int = 100
):
    return {"q": q, "skip": skip, "limit": limit}



@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons

