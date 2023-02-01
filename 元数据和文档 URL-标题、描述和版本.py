# 元数据和文档 URL-标题、描述和版本

# Title：在 OpenAPI 和自动API 文档用户界面中作为 API 的标题/名称使用。
# Description：在 OpenAPI 和自动 API 文档用户界面中用作 API 的描述。
# Version：API 版本，比如 v2 或者 v2.5.0.

from fastapi import FastAPI

description = """
Koala's APP API helps you do awesome stuff.

## Items

You can **read items**

## Users

You will be able to :

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""


app = FastAPI(
    title="Koala's APP",
    description=description,
    version="v0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Koala Wang",
        "url": "https://www.example.com/contact",
        "email": "koala.wangyang@qq.com",
    },
)


@app.get("/")
async def root():
    return {"message": "Welcome to Koala's APP"}