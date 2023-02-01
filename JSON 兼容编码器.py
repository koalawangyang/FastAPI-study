# JSON 兼容编码器
# 如果需要将 Pydantic 模型转换为与 JSON 兼容的数据类型（dict，list）等，比如存储到数据库中，则可以用 jsonable_encoder()

# 让我们假设你有一个数据库名为fake_db，它只能接收与JSON兼容的数据。
# 例如，它不接收datetime这类的对象，因为这些对象与JSON不兼容。
# 因此，datetime对象必须将转换为包含ISO格式化的str类型对象。
# 同样，这个数据库也不会接收Pydantic模型（带有属性的对象），而只接收dict。
# 对此你可以使用jsonable_encoder，接收一个对象，比如Pydantic模型，并会返回一个JSON兼容的版本。

from datetime import datetime
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None  # 和 Union 一样


app = FastAPI()

fake_db = {}

print(type(fake_db))

@app.put("/items/{id}")
async def update_item(id: str, item: Item): # 接收一个 Pydantic 数据类型
    json_compatible_item_date = jsonable_encoder(item) # 将其转换为 dict 类型
    fake_db[id] = json_compatible_item_date # 存储到 db 中
    return fake_db[id]

