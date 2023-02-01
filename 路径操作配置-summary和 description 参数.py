# 路径操作配置-summary和 description 参数

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/", summary="Read Items!", description="read all items~")
async def read_items():
    return "All items~"
