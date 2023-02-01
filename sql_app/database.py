# 数据库配置文件
# 导入 SQLAlchemy 部件
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 定义 SQLAlchemy 的数据库 URL 地址
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# 如果使用 PGSQL，则是这样的格式
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# 创建 SQLAlchemy 引擎，其中 check_same_thread 参数仅用于 SQLite，在其他数据库不需要。
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 创建 SessionLocal 类，将是实际的数据库会话。
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建 Base 类，稍后使用该类型继承，来创建每个数据库模型或ORM 模型。
Base = declarative_base()
