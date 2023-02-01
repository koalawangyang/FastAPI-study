# 处理错误-安装自定义异常处理器
# 假设要触发的自定义异常叫 UnicornException，且需要 FastAPI 实现全局处理该异常，此时可以用 @app.exception_handler() 添加自定义异常控制器。

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


app = FastAPI()


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something wrong."},
    )


@app.get("/unicorns/{name}")
async def read_unicorn_name(name: str):
    if name == "koala":
        raise UnicornException(name=name)
    return {"unicorn_name": name}
