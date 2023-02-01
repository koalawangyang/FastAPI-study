# 额外的模型-模型列表

from typing import List
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    description: str


items = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane", "age": 1},
]


@app.get("/items/", response_model=List[Item])
async def read_items():
    return items