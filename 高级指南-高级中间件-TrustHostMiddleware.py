# 高级指南-高级中间件-TrustHostMiddleware

from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI()
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["localhost", "*.example.com"])


@app.get("/")
async def main():
    return {"message": "Hello!"}