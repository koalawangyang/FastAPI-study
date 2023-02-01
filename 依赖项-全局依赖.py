# 依赖项-全局依赖
# 有时，需要为整个应用添加依赖项，此时可以采用类似[路径操作装饰器依赖项]的方式，把依赖项添加到整个 FastAPI 应用。

from fastapi import FastAPI, HTTPException, Header, Depends

async def verify_token(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token Header invalid!")


async def verify_key(x_key: str = Header()):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Secret Header invalid!")
    # 这里即便有返回值，实际也不会将返回值传递给路径操作函数
    return x_key


app = FastAPI(dependencies=[Depends(verify_token),Depends(verify_key)])


@app.get("/items/")
async def read_items():
    return [{"item": "Portal Gun"}, {"item": "Plumbus"}]


@app.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]