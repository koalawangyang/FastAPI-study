# 高级指南-自定义响应-UJSONResponse
# UJSONResponse 是一个使用 ujson 的可选 JSON 响应。
# 在处理某些边缘情况时，ujson 不如 Python 内置实现那么谨慎。
# pip install ujson
# ORJSONResponse 可能是一个更快的选择。

from fastapi import FastAPI
from fastapi.responses import UJSONResponse

app = FastAPI()


@app.get("/items/", response_class=UJSONResponse)
async def read_items():
    return [{"item_id": "Foo"}]