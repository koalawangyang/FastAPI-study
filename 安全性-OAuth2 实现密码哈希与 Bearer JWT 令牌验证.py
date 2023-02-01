# 安全性-OAuth2 实现密码哈希与 Bearer JWT 令牌验证
# 执行 pip install python-jose 在 Python 中生成和校验 JWT 令牌
# 执行 pip install passlib 处理密码哈希，教程中使用的是 Bcrypt 算法。
# 执行 pip install bcrypt 安装 Bcrypt 作为后端算法。

from datetime import datetime, timedelta

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from jose import JWTError, jwt
from passlib.context import CryptContext

from pydantic import BaseModel

# run this to get a Secret Key: openssl rand -hex 32
SECRET_KEY = "3c1ba465a71f06dce37d0f8dfa65e8ef610db5b12b7b6ad14cda115be60dd295"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 虚拟用户 DB
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    },
}


# Token 模型
class Token(BaseModel):
    access_token: str
    token_type: str


# Token 中数据的模型
class TokenData(BaseModel):
    username: str | None = None


# 用户模型
class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


# 用户存储在 DB 的模型
class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()


def verify_password(plain_password, hashed_password):
    """
    验证密码函数
    :param plain_password: 用户输入的密码
    :param hashed_password: 用户加密后的密码
    :return: 验证结果
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """
    对密码进行哈希加密
    :param password: 用户输入的密码
    :return: 哈希加密后的密码
    """
    return pwd_context.hash(password)


def get_user(db, username: str):
    """
    获取用户在DB中的数据
    :param db: 用户数据库
    :param username: 用户名
    :return: 用户在 DB 中存储的信息
    """
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def authenticate_user(fake_db, username: str, password: str):
    """
    验证用户信息
    :param fake_db: 虚拟用户 DB
    :param username: 用户名
    :param password: 用户密码
    :return: 如果验证失败，返回 False，如果验证通过，返回用户信息
    """
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
    创建授权密钥
    :param data:
    :param expires_delta: 过期时间
    :return: 返回编码后的 jwt
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    获取当前用户，依赖项为 oauth2_scheme
    :param token: 用户 token
    :return: 返回当前用户信息
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # 对 JWT 进行解码，传入 token、密钥、算法
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # 获取解码后的 sub 字段值，赋值给 username。
        username: str = payload.get("sub")
        # 如果用户名为空，则返回验证异常。
        if username is None:
            raise credentials_exception
        # 如果用户名不为空，将 username 传入 TokenData 模型
        token_data = TokenData(username=username)
    # 如果失败，则抛出验证异常。
    except JWTError:
        raise credentials_exception
    # 如果验证成功，则将虚拟用户 DB 和用户名传入 get_user 函数。
    user = get_user(fake_users_db, username=token_data.username)
    # 再查询用户 DB 中的用户是否存在，如果用户不存在，返回验证异常。
    if user is None:
        raise credentials_exception
    # 如果用户存在，则返回用户信息
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    """
    获取当前启用的用户。
    :param current_user: 当前用户，依赖于 get_current_user 函数，对当前用户的启用状态进行判断。
    :return: 当前处于启用的用户。
    """
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive User")
    return current_user


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm)):
    """
    登录并获取 token
    :param form_data: 用户表单数据
    :return: 用户授权密钥
    """
    # 调用 authenticate_user 函数，将用户表单中的用户名、密码传入
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    # 如果用户不存在，返回 401 错误码
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # 如果用户存在，对配置参数 ACCESS_TOKEN_EXPIRE_MINUTES 进行时间转换。
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # 将用户名、过期时间传入 create_access_token 函数，获取编码后的 JWT token。
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires,
    )
    # 将 token 返回
    return {"access_token": access_token, "token_type": "Bearer"}


@app.get("/users/me/", response_model=User)
async def user_home_page(current_user: User = Depends(get_current_active_user)):
    """
    用户主页
    :param current_user: 当前已激活用户
    :return: 返回当前已登录用户
    """
    return current_user


@app.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]
