# 高级指南-高级中间件-GZipMiddleware

from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()

# 当请求中包含"gzip"时，响应时会根据设定的大小启用 gzip 压缩，此处以 100 为例，当响应内容小于 100 时，不启用 gzip
# 当响应内容大于 100 时，启用 gzip，届时 response 里会有如下参数：
# Content-Encoding: gzip
app.add_middleware(GZipMiddleware, minimum_size=100)


@app.get("/")
async def main():
    return "somebigcontent"