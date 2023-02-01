# 静态文件

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


app = FastAPI()


# /static 路径下的所有请求都将由 static 静态目录来处理。
app.mount("/static", StaticFiles(directory="static"), name="static")
