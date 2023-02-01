# 高级指南-自定义响应-PlainTextResponse
# 接受文本或者字节并返回纯文本响应。

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/items/", response_class=PlainTextResponse)
async def read_items():
    return "Hello World."