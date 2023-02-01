# 表单数据
# 接收的不是 JSON，而是表单字段时，需要使用 Form，使用 pip install python-multipart 进行安装

from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username, "password": password}