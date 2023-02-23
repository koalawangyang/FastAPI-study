# 高级指南-OpenAPI 中更多响应-额外的媒体类型
# 在 response 参数中添加不同的媒体类型

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel


class Item(BaseModel):
    id: str
    value: str


app = FastAPI()


@app.get(
    "/items/{item_id}",
    response_model=Item,
    responses={
        200: {
            "content": {"file/py": {}},
            "description": "Return the JSON item or an image.",
        },
    },
)
async def read_items(item_id: str, img: bool | None = None):
    if img:
        return FileResponse("高级指南-OpenAPI 中更多响应-额外的媒体类型.py", media_type="file/py")
    return {"id": "foo", "value": "there goes my hero"}
