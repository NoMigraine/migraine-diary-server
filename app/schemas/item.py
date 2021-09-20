from typing import Optional, List

from pydantic import BaseModel


class ItemTagBase(BaseModel):
    id: int = 0


class ItemTag(ItemTagBase):
    name: Optional[str]
    level: Optional[int]


# Shared properties
class ItemBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    pain_minute: Optional[int] = None
    pain_level: Optional[int] = None
    sleep_quality: Optional[int] = None
    painful_number: Optional[int] = None
    painful_area: Optional[str] = None

    item_feel_tag: Optional[ItemTag]
    item_foreboding_tag: Optional[ItemTag]
    item_triggers_tag: Optional[ItemTag]
    item_complication_tag: Optional[ItemTag]
    item_affect_tag: Optional[ItemTag]
    item_relief_pain_tag: Optional[ItemTag]
    item_drug_tag: Optional[ItemTag]
    item_treatment_tag: Optional[ItemTag]
    item_emotions_tag: Optional[ItemTag]


# Properties to receive on item creation
class ItemCreate(ItemBase):
    title: str

    item_feel_tag: List[Optional[ItemTagBase]]
    item_foreboding_tag: List[Optional[ItemTagBase]]
    item_triggers_tag: List[Optional[ItemTagBase]]
    item_complication_tag: List[Optional[ItemTagBase]]
    item_affect_tag: List[Optional[ItemTagBase]]
    item_relief_pain_tag: List[Optional[ItemTagBase]]
    item_drug_tag: List[Optional[ItemTagBase]]
    item_treatment_tag: List[Optional[ItemTagBase]]
    item_emotions_tag: List[Optional[ItemTagBase]]


# Properties to receive on item update
class ItemUpdate(ItemBase):
    pass


# Properties shared by models stored in DB
class ItemInDBBase(ItemBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Item(ItemInDBBase):
    pass


# Properties properties stored in DB
class ItemInDB(ItemInDBBase):
    pass
