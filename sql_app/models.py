# SQLAlchemy 数据模型文件
# SQLAlchemy 模型使用 = 来定义熟悉，并将类型作为参数传递给 Column，比如：
# name = Column(String)

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


# 用户模型
class User(Base):
    # 表名
    __tablename__ = "users"

    # ID 属性，整数，主键，开启索引
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # 创建关系，通过 relationship 表示 users 表与 items 表有关系，反向引用的时候，用 owner
    items = relationship("Item", back_populates="owner")


# 类目模型
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    # 创建关系，表示 items 表与 users 表有关系，反向引用的时候，用 items
    owner = relationship("User", back_populates="items")


