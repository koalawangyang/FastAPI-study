# 依赖项-子依赖项

from fastapi import FastAPI, Depends, Cookie

app = FastAPI()


# 子依赖项
def query_extractor(q: str | None = None):
    return q


# 主依赖项
def query_or_cookie_extractor(q: str = Depends(query_extractor), last_query: str | None = Cookie(default=None)):
    print(f"q:{q}")
    if not q:
        print(f"last_query:{last_query}")
        return last_query
    return q


@app.get("/items/")
async def read_items(query_or_default: str | None = Depends(query_or_cookie_extractor)):
    return {"q_or_cookie": query_or_default}
