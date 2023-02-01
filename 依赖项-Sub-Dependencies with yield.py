# 依赖项-Sub-Dependencies with yield
# 子依赖项、依赖树中都可以使用 yield，比如本例中的 dependency_c 依赖于 dependency_b，dependency_b 依赖于 dependency_a。
# 本例中，dependency_c 执行退出时，需要 dep_b 的值，因而执行 dependency_b 函数（依赖项），而 dependency_b 函数退出时需要 dep_a 的值。

# 如果有 HTTP Exception 异常需要抛出，则不应当在 yield 之后抛出，因为 yield 出现异常时，将直接返回异常给客户端，此时响应信息已经发出，无法改变已经发出的响应信息。
# 因此，在 yield 之后通常执行一些需要后台处理的任务，比如关闭 db、将日志发送给远端追踪系统等。

from fastapi import Depends

async def dependency_a():
    dep_a = generate_dep_a()
    try:
        yield dep_a
    finally:
        dep_a.close()


async def dependency_b(dep_a = Depends(dependency_a)):
    dep_b = generate_dep_b()
    try:
        yield dep_b
    finally:
        dep_b.close(dep_a)


async def dependency_c(dep_b = Depends(dependency_b)):
    dep_c = generate_dep_c()
    try:
        yield dep_c
    finally:
        dep_c.close(dep_b)
