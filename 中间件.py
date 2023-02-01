# 中间件
# "中间件"是一个函数，它在每个 http 请求 被特定的路径操作函数 处理之前，以及在每个 http 响应 返回之前 工作。
# ● 它接收你的应用程序的每一个请求。
# ● 然后它可以对这个请求做一些事情或者执行任何需要的代码。
# ● 然后它将请求传递给应用程序的其他部分（通过某种路径操作函数）。
# ● 然后它获取应用程序生产的响应。
# ● 它还可以对该响应做些操作或者执行任何需要的代码。
# ● 最终它返回这个响应。
# ● 如果使用了 yield 关键字依赖，依赖中的退出代码将在执行中间件后执行。
# ● 如果有任何后台任务，它们将在执行中间件后运行。


import time
from fastapi import FastAPI, Request

app = FastAPI()


# 固定写法
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """
    添加处理时间的 Header
    :param request: 固定写法，接收 request
    :param call_next: 固定写法，接收 request 作为参数，传递给响应的路径操作函数，然后返回 response。
    :return: 固定写法，将 response 返回。
    """
    # 获取处理的起始时间
    start_time = time.time()
    # 调用路径操作函数处理请求
    response = await call_next(request)
    # 处理时间 = 处理后的当前时间 - 起始时间
    process_time = time.time() - start_time
    # 在 response 的 header 中添加 处理时间的 参数
    response.headers["X-Process-Time"] = str(process_time)
    response.headers["X-Koala-Added"] = "Testing~"
    return response


@app.get("/items/")
async def read_items():
    return {"Hello, FastAPI!"}
