# 高级指南-自定义响应-FileResponse
# 异步传输文件作为响应
# 与其他响应类型相比，接受不同的参数集进行实例化：
# path: 要流式传输的文件的路径
# headers: 任何自定义响应头，传入 dict 类型
# media_type: 给出媒体类型的字符串。如果未设置，则文件名或路径将用于推断媒体类型。
# filename: 如果给出，它将包含在相应的 Content-Disposition 中

# 文件相应将包含适当的 Content-Length，Last-Modified 和 ETag 的响应头。

from fastapi import FastAPI
from fastapi.responses import FileResponse

some_file_path = "large-video-file.mp4"
app = FastAPI()


@app.get("/", response_class=FileResponse)
async def main():
    return FileResponse(some_file_path)

 # content-length: 0
 # content-type: video/mp4
 # date: Wed,01 Feb 2023 09:17:16 GMT
 # etag: 0280803dc8e84d20ccbd391ffcabaf77
 # last-modified: Wed,01 Feb 2023 09:11:26 GMT
 # server: uvicorn