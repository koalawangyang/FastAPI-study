# 高级指南-直接返回响应-返回 XML

from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/legacy/")
async def get_legacy_data():
    data = """
    <?xml version="1.0"?>
    <shampoo>
    <Header>
        Apply shampoo here.
    <Eye>
        Watch your Eyes.
    </Eye>
    </Header>
    <Body>
        You'll have to use soap here.
    </Body>
    </shampoo>
    """

    return Response(content=data, media_type="application/xml")
