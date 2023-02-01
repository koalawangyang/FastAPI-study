# 请求体-更新数据-PUT
# 更新数据使用 PUT 操作。
# 输入的数据要转换为以 JSON 格式存储的数据时，使用 jsonable_encoder，例如，把 datetime 转换为 str。

from typing import List, Union
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


class Item(BaseModel):
    name: Union[str, None] = None
    description: str | None = None
    price: float | None = None
    tax: float = 10.5
    tags: List[str] = []


app = FastAPI()


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 105.2, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 21.4, "tax": 13.4, "tags": ["New","York"]}
}

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    update_item_encoder = jsonable_encoder(item)  # 将接收到的 JSON 转换为 dict
    items[item_id] = update_item_encoder # 替换现有的数据
    return items[item_id] # 返回更新后的数据


# PUT 操作将更新全部数据，如果请求体中未包含所有字段，则使用默认值填充，如果要更新部分数据，则应该使用 PATCH 操作。