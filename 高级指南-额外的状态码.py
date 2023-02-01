# 高级指南-额外的状态码
# 如果想要返回主要状态码之外的状态码，可以通过返回一个 Response 类实现，比如 JSONResponse，然后设置额外的状态码
# 本示例中，使用同一个 put 方法实现即可以更新也可以创建数据：
# 如果目标 item_id 已存在，则更新现有值，返回 200 [成功]
# 如果目标 item_id 不存在，则创建新值，返回 201 [已创建]

from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse


app = FastAPI()

items = {
    "foo": {
        "name": "Fighters",
        "size": 6,
    },
    "bar": {
        "name": "Tenders",
        "size":8,
    },
}


@app.put("/items/{item_id}")
async def upsert_item(
        item_id: str,
        name: str | None = Body(default=None),
        size: int | None = Body(default=None),
):
    if item_id in items:
        item = items[item_id]
        item["name"] = name
        item["size"] = size
        return item
    else:
        item = {"name": name, "size": size}
        items[item_id] = item
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=item)
