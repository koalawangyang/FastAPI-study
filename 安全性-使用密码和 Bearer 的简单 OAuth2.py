# 安全性-使用密码和 Bearer 的简单 OAuth2

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from pydantic import BaseModel


app = FastAPI()

# 虚拟用户 DB
fake_users_db = {
    "johndoe":{
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}


# 生成虚拟加密密码函数
def fake_hashed_password(password: str):
    return "fakehashed" + password


# 创建 OAuth2 密码实例
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# 用户数据模型，不含密码
class User(BaseModel):
    username: str
    full_name: str | None = None
    email: str | None = None
    disabled: bool | None = None


# 用户在数据库的数据模型，含密码，该模型集成 用户模型
class UserInDB(User):
    hashed_password: str


def get_user(db, username: str):
    """
    获取用户函数
    :param db: 用户数据库
    :param username: 用户名
    :return: 如果用户名存在于数据库，则返回用户在数据库的数据模型中的数据。
    """
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    """
    虚拟解密用户 token 函数，该函数获取用户token（其实是用户名），并直接在数据库查找
    :param token: 用户 token 值，在这里实际是用户名
    :return: 返回用户信息
    """
    # 将虚拟用户 DB 和 token 传入 获取用户 函数
    user = get_user(fake_users_db, token)
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    获取当前用户函数
    :param token: 执行依赖项 oauth2_scheme
    :return: 返回用户数据
    """
    # 调用虚拟解密用户函数
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Authentication Credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    """
    获取当前激活用户函数，检查用户是否启用
    :param current_user: 当前用户，Pydantic 类型，依赖项为获取当前用户
    :return:
    """
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive User")
    return current_user


@app.post("/token")
async def login(form_date: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm)):
    """
    用户登录函数
    :param form_date: 表单数据，依赖项为OAuth2PasswordRequestForm。
    :return: 返回用户名
    """
    # 将表单中的用户名带入虚拟用户 DB 进行查找
    user_dict = fake_users_db.get(form_date.username)
    # 如果用户不存在，返回 400 错误
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect Username or Password")
    # 如果用户存在，将表单中的用户数据解包并传入 UserInDB 函数
    user = UserInDB(**user_dict)
    # 调用虚拟加密函数，对表单中的用户密码进行加密
    hashed_password = fake_hashed_password(form_date.password)
    # 对比用户提交的密码加密与数据库中存储的用户密码
    if not hashed_password == user.hashed_password:
        # 如果不一致，返回 400 错误
        raise HTTPException(status_code=400, detail="Incorrect Username or Password")
    # 如果一致，返回用户名等信息。
    return {"access_token": user.username, "token_type": "bearer"}



@app.get("/users/me")
async def read_me(current_user: User = Depends(get_current_active_user)):
    """
    用户个人主页，获取当前激活用户。

    :param current_user: 数据类型为 User，依赖项为 get_current_active_user 。

    :return: 返回当前用户
    """
    return current_user