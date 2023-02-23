# 高级指南-Response Headers

from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse

app = FastAPI()


# 通过 response 参数来添加 headers
@app.get("/headers-and-object/")
def get_headers(response: Response):
    response.headers["X-Cat-Dog"] = "alone in the world"
    return {"message": "Hello World"}


# 在返回 Response 的时候直接添加 headers
@app.get("/headers/")
def get_header():
    content = {"message": "Hello world"}
    headers = {"X-Cat-Dog": "alone in the world", "Content-Language": "en-US"}
    return JSONResponse(content=content, headers=headers)


# 自定义 Headers 以 'X-' 为前缀，后面每个单词首字母大写
# 如果想要在客户端浏览器中看到自定义 Headers，需要在 CORS 配置中添加。