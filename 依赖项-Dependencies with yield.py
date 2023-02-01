# 依赖项-Dependencies with yield
# FastAPI 支持依赖项在完成时做一些额外的操作，通过使用 yield 替换 return ，然后在 yield 之后写上额外需要执行的步骤。
# 确保只使用一次 Yield

# aync def get_db():
#     # 发送响应前将先执行这段以及下面的 yield 代码。
#     db = DBSession()
#     try:
#         yield db  # yield 的值将被注入到路径操作和其他依赖项中。
#     # yield 后面的内容将在交付响应后执行。
#     finally:
#         db.close()

