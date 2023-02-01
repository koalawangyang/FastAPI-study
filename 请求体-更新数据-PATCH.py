# 请求体-更新数据-PATCH
# PATCH 没有 PUT 知名，也不怎么常用，很多人甚至使用 PUT实现部分更新，FASTAPI对此没有限制，可以随时使用这两种操作。
# 更新部分数据时，可以在 Pydantic 模型的 .dict() 中使用 exclude_unset 参数，比如 item.dict(exclude_unset=True)
# 这段代码生成的 dict 只包含创建 item 模型时显式设置的数据，而不包括默认值。
# 然后再用它生成一个只包含已设置（在请求中发送）数据，且省略了默认值的 dict。

# 注意，输入模型仍需验证。
# 因此，如果希望接收的部分更新数据可以省略其他所有属性，则要把模型中所有的属性标记为可选（使用默认值或者 None）。

from typing import List, Union
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


class Item(BaseModel):
    name: Union[str, None] = None
    description: Union[str, None] = None
    price: Union[float, None] = None
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


app = FastAPI()


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@app.patch("/items/{item_id}", response_model=Item)
async def patch_item(item_id: str, item: Item):
    stored_item_data = items[item_id] # 先获取要更新的 item 当前的数据
    stored_item_model = Item(**stored_item_data) # 将 item 当前的数据解包，传入 Item 模型
    update_data = item.dict(exclude_unset=True) # 将请求体中仅更新的字段提取出来
    update_item = stored_item_model.copy(update=update_data) # 将仅更新的字段更新到含有当前数据的 Item 模型副本中
    items[item_id] = jsonable_encoder(update_item) # 再将 Pydantic 模型转换为 JSON 格式
    return update_item


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    update_item_data = jsonable_encoder(item)
    items[item_id] = update_item_data
    return items[item_id]



