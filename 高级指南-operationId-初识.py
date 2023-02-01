# 高级指南-operationId-初识
# 可以在路径操作中通过参数 operation_id 设置要使用的 OpenAPi operationId。
# 务必确保每个操作路径的 operation_id 是唯一的。
# 暂时还不明白 operationId 的作用，仅使用最简单的示例，若要了解更多，参考 https://fastapi.tiangolo.com/zh/advanced/path-operation-advanced-configuration/

from fastapi import FastAPI

app = FastAPI()

# 使用 incluse_in_schema = False 来排除一个路径操作。
# @app.get("/items/", operation_id="some_specific_id_you_define", include_in_schema=False)
@app.get("/items/", operation_id="some_specific_id_you_define")
async def read_items():
    return [{"item_id": "Foo"}]
