# 元数据和文档 URL-标签元数据
# 使用参数 openapi_tags，为用于分组路径操作的不同标签添加额外的元数据。

from fastapi import FastAPI

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external dcos",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

app = FastAPI(
    openapi_tags=tags_metadata,
    # 更改 Swagger UI 文档 URL
    docs_url="/api/docs",
    # 更改 ReDoc 文档 URL
    redoc_url="/api/redoc",
    # OpenAPI 模式地址了进行更改
    openapi_url="/api/v1/openapi.json",
    # 也可以禁用 OpenAPI 模式
    # openapi_url=None,
)


@app.get("/users/", tags=["users"])
async def get_users():
    return [{"name": "Harry"}, {"name": "Ron"}]


@app.get("items/", tags=["items"])
async def get_items():
    return [{"name": "wand"}, {"name": "flying broom"}]
