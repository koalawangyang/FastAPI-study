# 高级指南-自定义响应-RedirectResponse
# 返回 HTTP 重定向，默认情况下使用 307 状态码（临时重定向）

from fastapi import FastAPI
from fastapi.responses import RedirectResponse


app = FastAPI()


@app.get("/items/", response_class=RedirectResponse)
async def redirect_response():
    return RedirectResponse("https://www.qq.com/")