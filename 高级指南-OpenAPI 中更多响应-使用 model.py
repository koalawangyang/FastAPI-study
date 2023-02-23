# 高级指南-OpenAPI 中更多响应-使用 model
# 在路径操作注解中传递一个 response 参数
# 该参数接收一个字典，键为 状态码，值为另外一个字典，字典里是响应信息
# 每个响应字典里可以有一个 model 键，包含一个 Pydantic 数据模型，就像 response_model.

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class Item(BaseModel):
    id: str
    value: str


class Message404(BaseModel):
    message: str


app = FastAPI()


@app.get(
    "/items/{item_id}",
    response_model=Item,
    responses={
        404: {
            "model": Message404,
        },
    },
)
async def read_item(item_id: str):
    if item_id == "foo":
        return {"id": "foo", "value": "there goes my hero"}
    return JSONResponse(status_code=404, content={"message": "Item not found", "more": "some"})