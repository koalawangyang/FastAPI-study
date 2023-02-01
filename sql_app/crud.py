# CRUD 工具，编写可重用的函数，用来与数据库中的数据进行交互。
# CRUD 分别是：创建、查询、更改和删除，即增删改查。本示例中只是新增和查询。
# 创建仅用于与数据库交互的函数，独立于路径操作函数，可以更轻松地在多个部分中重用它们，并为它们添加单元测试。

from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    """
    通过 user_id 查询用户。
    :param db: 数据库会话
    :param user_id: 被查询的用户 ID
    :return: 查询结果
    """
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    """
    通过 email 查询用户。
    :param db: 数据库会话
    :param email: 被查询的用户 email
    :return: 查询结果
    """
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """
    查询所有用户。
    :param db: 数据库会话
    :param skip: 查询起始值
    :param limit: 查询限制值
    :return: 所有查询范围内的用户
    """
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    """
    创建用户。
    :param db: 数据库会话
    :param user: 需要被创建的用户
    :return: 创建结果
    """
    # 虚拟哈希密码
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    """
    获取指定范围的类目
    :param db: 数据库会话
    :param skip: 范围起始值
    :param limit: 范围结束值
    :return: 范围内的类目
    """
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    """
    创建用户的类目。
    :param db: 数据库会话
    :param item: 需要创建的类目
    :param user_id: 用户 ID
    :return: 创建结果
    """
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


