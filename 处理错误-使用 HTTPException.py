# 处理错误-使用 HTTPException
# 向客户端返回 HTTP 错误响应，可以使用 HTTPException
from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"koala": "wang", "name": "666"}


@app.get("/items/{item_id}")
async def read_item(item_id:str = None):
    if item_id not in items:
        # 可以添加自定义 Header 响应头
        raise HTTPException(status_code=404, detail="Item not found", headers={"X-Error": "DIY error header"})
    else:
        return {"item": items[item_id]}

