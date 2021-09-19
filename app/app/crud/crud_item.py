import datetime
from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import models
from app.crud.base import CRUDBase
from app.models.item import Item
from app.schemas.item import ItemCreate
from app.schemas.item import ItemUpdate

table_name_model_map = {
    'item_feel_tag': models.FeelTag,
    'item_foreboding_tag': models.ForebodingTag,
    'item_triggers_tag': models.TriggersTag,
    'item_complication_tag': models.ComplicationTag,
    'item_affect_tag': models.AffectTag,
    'item_relief_pain_tag': models.ReliefPainTag,
    'item_treatment_tag': models.TreatmentTag,
    'item_emotions_tag': models.EmotionsTag,
    'item_drug_tag': models.DrugTag,
}


class CRUDItem(CRUDBase[Item, ItemCreate, ItemUpdate]):
    def create_with_owner(
            self, db: Session, *, obj_in: ItemCreate, owner_id: int
    ) -> Item:
        obj_in_data = jsonable_encoder(obj_in)
        time_now = str(datetime.datetime.now())
        obj_in_data['create_time'], obj_in_data['update_time'] = time_now, time_now
        new_obj_in_data = {}
        for k, v in obj_in_data.items():
            if isinstance(v, list):
                # 如果是多对多则自动将id实例化为对应model，以便于自动填充中间表
                tag_ids = [i.get('id') for i in v] if v else []
                new_obj_in_data[k] = db.query(table_name_model_map[k]).filter(
                    table_name_model_map[k].id.in_(tag_ids)).all()
            else:
                new_obj_in_data[k] = v

        db_obj = self.model(**new_obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
            self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[Item]:
        return (
            db.query(self.model).filter(Item.owner_id == owner_id).offset(skip).limit(limit).all()
        )


item = CRUDItem(Item)
