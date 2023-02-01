# Testing-TestClient
# 通过 pip install httpx 来安装 httpx，然后才能使用 TestClient
# 最后安装 pytest
# pip install pytest

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
