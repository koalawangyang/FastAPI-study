# 高级指南-自定义响应-HTML、流、文件和其他-HTML响应
# 使用 HTMLResponse 来从 FastAPI 中直接返回一个 HTML 响应。
# 导入 HTMLResponse
# 将 HTMLResponse 作为路径操作的 response_class 参数传入。

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/items/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here.
            </title>
        </head>
        <body>
            <h1> Look ma! HTML!</h1>
        </body>
    </html>
    """


@app.get("/users/", response_class=HTMLResponse)
async def read_users():
    response_html = """
    <html>
        <head>
            <title>A DIY HTML Response
            </title>
        </head>
        <body>
            <h1> Look here!
            </h1>
        </body>
    </html>
    """
    return HTMLResponse(content=response_html, status_code=200)