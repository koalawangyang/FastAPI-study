# 额外的模型-Union 或 anyOf

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type: str = "car"


class PlaneItem(BaseItem):
    type: str = "plane"
    size: int


items = {
    "item1": {
        "description": "All my friends drive a low rider",
        "type": "car",
    },
    "item2": {
        "description": "Music is my areoplane, it's my areoplane",
        "type": "plane",
        "size": 5,
    },
}


@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def get_items(item_id: str):
    return items[item_id]
