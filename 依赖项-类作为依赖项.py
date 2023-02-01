# 依赖项-类作为依赖项

from fastapi import FastAPI, Depends

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


app = FastAPI()


class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
async def read_item(params: CommonQueryParams = Depends(CommonQueryParams)):
    response = {}
    if params.q:
        response.update({"q": params.q})
    items = fake_items_db[params.skip : params.skip + params.limit]
    response.update({"items": items})
    return response

