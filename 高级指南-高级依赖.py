# 高级指南-高级依赖

from fastapi import FastAPI, Depends

app = FastAPI()


class FixedContentQueryChecker:
    def __init__(self, fixed_content: str):
        self.fixed_content = fixed_content

    def __call__(self, q: str = ""):
        if q:
            return self.fixed_content in q
        return False


checker = FixedContentQueryChecker("bar")


@app.get("/query-checker/")
async def query(fixed_content_included: bool = Depends(checker)):
    return {"fixed_content_in_query": fixed_content_included}