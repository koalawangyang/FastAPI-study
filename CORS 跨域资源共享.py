# CORS 跨域资源共享

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://localhost",
    "https://localhost:8080",
]


app.add_middleware(
    CORSMiddleware,
    # 允许的源列表
    allow_origins=origins,
    # 凭证（授权 headers，Cookies 等）
    allow_credentials=True,
    # 允许的方法，比如 Post、Put、Get 等
    allow_methods=['PUT'],
    # 允许的 headers
    allow_headers=["*"],
)


@app.put("/you")
async def main():
    return {"message": "Hello FastAPI!"}


@app.get("/me")
async def read_me():
    return {"message": "Me!"}


