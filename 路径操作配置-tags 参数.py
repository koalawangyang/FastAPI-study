# 路径操作配置-tags 参数
# tags参数的值是由 str 组成的list，一般只有一个 str，tags 用于为路径操作添加标签，这里的标签可以理解为文档中的章节

from fastapi import FastAPI

app = FastAPI()


@app.get("/users/", tags=["User Section"])
async def read_users():
    return "All users, not really~"


@app.get("/items/", tags=["Item Section", "Item Section Two"])
async def read_item():
    return "All items, not really~"


