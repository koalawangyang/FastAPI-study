# 高级指南-自定义响应-StreamingResponse-初识
# 采用异步生成器或普通生成器/迭代器，然后刘师传输响应主体。
# 对类型文件的对象使用 StreamingResponse
# 比如，由 open()返回的对象，则可以在 StreamingResponse 中将其返回，包括许多与云存储、视频处理相关的库
# 具体示例查看下面一章

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


async def fake_video_streamer():
    for i in range(10):
        yield b"some fake video bytes"

@app.get("/items/")
async def read_items():
    return StreamingResponse(fake_video_streamer())

