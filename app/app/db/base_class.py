from typing import Any

from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.ext.declarative import declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        # return cls.__name__.lower()  # 这个方法导致长表名无_分割

        lst = []
        for index, char in enumerate(cls.__name__):
            if char.isupper() and index != 0:
                lst.append("_")
            lst.append(char)

        return "".join(lst).lower()

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if (
                hasattr(self, key) and key != "id" and value is not None
            ):  # 此处对用户添加的数据进行非空限制
                setattr(self, key, value)

    def __getitem__(self, item):
        return getattr(self, item)
