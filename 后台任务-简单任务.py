# 后台任务-简单任务
# 如果在返回请求后，需要做一些后台的任务，客户端不需要等待后台任务完成的情况下会比较有用，比如：
# 1. 客户端发起某个操作后需要发送邮件通知：如果等待邮件发送完成再返回响应给客户端，则会比较慢，可以立刻返回响应给客户端，然后在后台发送通知邮件。
# 2. 处理数据：例如接收一个文件会比较慢，此时可以返回"已收到"，然后在后台继续接收。

# 从 fastapi 导入 BackgroundTasks

from fastapi import FastAPI, BackgroundTasks

app = FastAPI()


def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some context")
    return {"message": "Notification sent in the background"}
