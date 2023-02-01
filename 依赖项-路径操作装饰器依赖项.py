# 依赖项-路径操作装饰器依赖项
# 如果依赖项不返回值，但仍需要执行，此时就可以使用路径操作装饰器里的由 dependencies 组成的 list 来使用依赖项

from fastapi import FastAPI, Depends, HTTPException, Header

app = FastAPI()


async def verify_token(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token Header invalid!")


async def verify_key(x_key: str = Header()):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key Header invalid!")
    return x_key


# 就算依赖项有返回值，也不会将返回值传递给路径操作函数
@app.get("/items/", dependencies=[Depends(verify_key), Depends(verify_token)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]
