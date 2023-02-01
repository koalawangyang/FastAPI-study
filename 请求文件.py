# 请求文件
# 上传文件将以【表单数据】形式发送，所以接收上传的文件，需要预先安装 pip install python-multipart


from fastapi import FastAPI, File, UploadFile
from typing import Union, List


app = FastAPI()


# 如果 file 类型声明为 bytes，则文件作为【表单数据】上传，且文件存储在内存里，适用于小型文件，不过很多情况下，UploadFile 更好用。
# 详情查看文档：https://fastapi.tiangolo.com/zh/tutorial/request-files/
@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


# UploadFile 相比 bytes 更有优势：
# 使用 spooled 文件，当存储在内存的文件超过最大上限时，FastAPI 会把文件存入磁盘。
# 更适合处理图像、视频、二进制文件等大型文件，好处是不会占用所有内存。
# 可获取上传文件的元数据。
# 自带 file-like async 接口。
# 暴露的 Python SpooledTemporaryFile 对象，可直接传递给其他预期 【file-like】对象的库。


# 可选文件上传

@app.post("/files/optional/")
async def create_file_optional(file: bytes | None = File(default=None)):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}


@app.post("/uploadfile/optional/")
async def create_upload_file_optional(file: Union[UploadFile, None] = None):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_name": file.filename}


# 带有额外元数据的 UploadFile，将 File() 和 Uploadfile 一起使用。
@app.post("/files/moredata")
async def create_file_moredata(file: bytes = File(description="A file read as bytes")):
    return {"filesize": len(file)}


@app.post("/uploadfile/moredata")
async def create_upload_file_moredata(file: UploadFile = File(description="A file read as UploadFile")):
    return {"filename": file.filename}


# 多文件上传
# 声明含有 bytes 或 UploadFile 的列表 List
@app.post("/files/multifiles")
async def create_file_multifiles(files: List[bytes] = File()):
    return {"filesizes": [len(file) for file in files]}
    # file_size_list = []
    # for file in files:
    #     file_size_list.append(len(file))
    # return file_size_list


@app.post("/uploadfile/multifiles")
async def create_upload_file_multi(files: List[UploadFile]):
    return {"filenames": [file.filename for file in files]}
