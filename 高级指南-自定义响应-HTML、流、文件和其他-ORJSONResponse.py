# 高级指南-自定义响应-HTML、流、文件和其他-ORJSONResponse
# 如果需要压榨性能，可以安装并使用 orjson 并将响应设置为 ORJSONResponse，导入并在路径操作装饰器中声明它。
# pip install orjson

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse


app = FastAPI()


@app.get("/items/", response_class=ORJSONResponse)
async def read_items():
    content = [{"name": "KoalaWang"}]
    return ORJSONResponse(content)

