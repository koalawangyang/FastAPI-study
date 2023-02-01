# 处理错误-覆盖默认异常控制器-覆盖请求验证异常
# 请求中包含无效数据时，FastAPI 将触发 RequestValidationError
# 该异常也内置了默认异常处理器。
# 覆盖默认异常处理器时需要导入 RequestValidationError，并用 @app.exception_handler(RequestValidationError) 装饰异常处理器。
# 这样，异常处理器就可以接收 Request 与异常。

from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return PlainTextResponse(str(exc), status_code=400)


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3!")
    return {"item_id": item_id}


