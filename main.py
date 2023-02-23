# 高级指南-直接使用 Request

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/items/{item_id}")
def 