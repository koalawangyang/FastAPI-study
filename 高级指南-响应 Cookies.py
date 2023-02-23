# 高级指南-响应 Cookies

from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/cookie-and-object/")
async def create_cookie(response: Response):
    response.set_cookie(key="fakesession", value="fake-cookie-session-value")
    return {"message": "Come to the dark side, we have cookies"}


# 另外一种写法，直接响应 Response 时直接创建 Cookies。
@app.get("/cookie/")
async def create_cookies():
    content = {"message": "Come to the dark side, we have cookies!"}
    response = JSONResponse(content=content)
    response.set_cookie(key="fakesession", value="fake-cookie-session-value")
    return response
