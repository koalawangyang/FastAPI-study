# 高级指南-自定义响应-StreamingResponse-高级

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

some_file_path = "large-video-file.mp4"
app = FastAPI()


@app.get("/")
# 这里使用的是不支持 async 和 await 的标准 open()，我们使用普通的 def 声明了路径操作。
def main():
    def iterfile():     # (1)
        with open(some_file_path, mode="rb") as file_like:  # (2)
            yield from file_like    # (3)

    return StreamingResponse(iterfile(), media_type="video/mp4")
