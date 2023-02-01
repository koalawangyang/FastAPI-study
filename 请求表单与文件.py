# 请求表单与文件

from fastapi import FastAPI, File, UploadFile, Form

app = FastAPI()


@app.post("/uploadfile/")
async def upload_file(file:bytes = File(), uploadfile: UploadFile = File(), token: str = Form()):
    return {
        "filesize": len(file),
        "file_content_type": uploadfile.content_type,
        "token": token,
    }

