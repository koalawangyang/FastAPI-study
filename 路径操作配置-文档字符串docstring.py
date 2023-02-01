# 路径操作配置-文档字符串docstring
# 如果 description 内容较多，会占用多行时，可以在函数的 docstring 中声明路径操作的描述，文档字符串支持 Markdown，但要注意缩进。

from typing import Set, Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()


@app.post("/items/", response_model=Item, summary="Create an item!", tags=["Items"])
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item
