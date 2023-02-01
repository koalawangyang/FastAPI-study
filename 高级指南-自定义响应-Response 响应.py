# 高级指南-自定义响应-Response 响应
# Response 类接受如下参数：
# content: 一个 str 或者 bytes
# status_code: 一个 int 类型的 HTTP 状态码
# headers: 一个由字符串组成的 dict
# media_type: 一个给出媒体类型的 str，比如"text/html"

from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/items/")
async def get_legacy_data():
    data = """
    <?xml version="1.0"?>
    <shampoo>
    <Header>
        Apply shampoo here.
    </Header>
    <Body>
        You'll have to use soap here.
    </Body>
    </shampoo>
    """
    return Response(content=data, media_type="application/xml")

