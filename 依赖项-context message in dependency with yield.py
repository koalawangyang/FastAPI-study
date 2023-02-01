# 依赖项-context message in dependency with yield
# 通过 __enter__() 和 __exit__() 来创建一个上下文消息。

class MySuperContextMessager:
    def __init__(self):
        self.db = DBSession()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()


async def get_db():
    # 该方式类似于 Python 中的文件打开，with open xxx，最终code block 完成后将自动关闭文件，而不需要自行编写代码来关系。
    with MySuperContextMessager() as db:
        # yield 执行时，将执行 MySuperContextMessager 中的 __enter__() 函数。
        # yield 完成后，将执行 MySuperContextMessager 中的 __exit__() 函数。
        yield db

