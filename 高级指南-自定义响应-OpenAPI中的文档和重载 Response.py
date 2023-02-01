# 高级指南-自定义响应-OpenAPI中的文档和重载 Response
# 如果想在函数内重载响应，但是在 OpenAPi 中文档化【媒体类型】，可以使用response_class 参数并返回一个 Response 对象。
# 接着response_class 参数只会被用来文档化 OpenAPi 的路径操作，你的 Response 用来返回响应。

from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


def generate_html_response():
    html_content = """
    <html>
        <head>
            <title>Some HTML codes here</title>
        </head>
        <body>
            <h1> Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


# 定义响应类为 HTMLResponse
@app.get("/items/", response_class=HTMLResponse)
async def read_items():
    # 调用 generate_html_response 函数并将结果返回。
    return generate_html_response()