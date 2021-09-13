from typing import TYPE_CHECKING

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401

# 中间表
item_feel_tag = Table(
    "item_feel_tag",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("item_id", Integer, ForeignKey("item.id"), nullable=False, primary_key=True),
    Column(
        "feel_tag_id",
        Integer,
        ForeignKey("feel_tag.id"),
        nullable=False,
        primary_key=True,
    ),
)

item_foreboding_tag = Table(
    "item_foreboding_tag",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("item_id", Integer, ForeignKey("item.id"), nullable=False, primary_key=True),
    Column(
        "foreboding_tag_id",
        Integer,
        ForeignKey("foreboding_tag.id"),
        nullable=False,
        primary_key=True,
    ),
)

item_triggers_tag = Table(
    "item_triggers_tag",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("item_id", Integer, ForeignKey("item.id"), nullable=False, primary_key=True),
    Column(
        "triggers_tag_id",
        Integer,
        ForeignKey("triggers_tag.id"),
        nullable=False,
        primary_key=True,
    ),
)

item_complication_tag = Table(
    "item_complication_tag",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("item_id", Integer, ForeignKey("item.id"), nullable=False, primary_key=True),
    Column(
        "complication_tag_id",
        Integer,
        ForeignKey("complication_tag.id"),
        nullable=False,
        primary_key=True,
    ),
)

item_affect_tag = Table(
    "item_affect_tag_tag",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("item_id", Integer, ForeignKey("item.id"), nullable=False, primary_key=True),
    Column(
        "affect_tag_id",
        Integer,
        ForeignKey("affect_tag.id"),
        nullable=False,
        primary_key=True,
    ),
)

item_relief_pain_tag = Table(
    "item_relief_pain_tag",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("item_id", Integer, ForeignKey("item.id"), nullable=False, primary_key=True),
    Column(
        "reliefpain_tag_id",
        Integer,
        ForeignKey("relief_pain_tag.id"),
        nullable=False,
        primary_key=True,
    ),
)

item_drug_tag = Table(
    "item_drug_tag",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("item_id", Integer, ForeignKey("item.id"), nullable=False, primary_key=True),
    Column(
        "drug_tag_id",
        Integer,
        ForeignKey("drug_tag.id"),
        nullable=False,
        primary_key=True,
    ),
)

item_treatment_tag = Table(
    "item_treatment_tag",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("item_id", Integer, ForeignKey("item.id"), nullable=False, primary_key=True),
    Column(
        "treatment_tag_id",
        Integer,
        ForeignKey("treatment_tag.id"),
        nullable=False,
        primary_key=True,
    ),
)

item_emotions_tag = Table(
    "item_emotions_tag",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("item_id", Integer, ForeignKey("item.id"), nullable=False, primary_key=True),
    Column(
        "emotions_tag_id",
        Integer,
        ForeignKey("emotions_tag.id"),
        nullable=False,
        primary_key=True,
    ),
)


# query = Video.query.filter(Video.tag.any(Tag.id == tag_id))


class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    pain_minute = Column(Integer, nullable=True, comment="疼痛时常，以分钟为单位，原头痛开始结束时间")
    pain_level = Column(Integer, nullable=True, comment="疼痛等级/10级")
    sleep_quality = Column(Integer, nullable=True, comment="睡眠质量/10级")
    painful_number = Column(Integer, nullable=True, comment="头痛次数/天")
    painful_area = Column(String, nullable=True, comment="头痛部位")
    create_time = Column(DateTime)
    # create_time = Column(DateTime, server_default=func.now(), nullable=False)  # sqlite 不支持func.now()，迁就一下  # noqa
    update_time = Column(DateTime)

    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="items")
    item_feel_tag = relationship("FeelTag", secondary=item_feel_tag, backref="items")
    item_foreboding_tag = relationship("ForebodingTag", secondary=item_foreboding_tag, backref="items")
    item_triggers_tag = relationship("TriggersTag", secondary=item_triggers_tag, backref="items")
    item_complication_tag = relationship("ComplicationTag", secondary=item_complication_tag, backref="items")
    item_affect_tag = relationship("AffectTag", secondary=item_affect_tag, backref="items")
    item_relief_pain_tag = relationship("ReliefPainTag", secondary=item_relief_pain_tag, backref="items")
    item_drug_tag = relationship("DrugTag", secondary=item_drug_tag, backref="items")
    item_treatment_tag = relationship("TreatmentTag", secondary=item_treatment_tag, backref="items")
    item_emotions_tag = relationship("EmotionsTag", secondary=item_emotions_tag, backref="items")


class BaseTag(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    level = Column(Integer, nullable=True, comment="标签顺序等级")


class FeelTag(BaseTag):
    """疼痛感受标签"""


class ForebodingTag(BaseTag):
    """先兆标签"""


class TriggersTag(BaseTag):
    """诱因标签"""


class ComplicationTag(BaseTag):
    """并发症状标签"""


class AffectTag(BaseTag):
    """对生活的影响标签"""


class ReliefPainTag(BaseTag):
    """缓解头痛手段标签"""


class DrugTag(BaseTag):
    """药物标签"""


class TreatmentTag(BaseTag):
    """治疗手段标签"""


class EmotionsTag(BaseTag):
    """情绪标签"""
