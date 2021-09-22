from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.item import create_random_item


def test_create_item(
        client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    data = {
        "title": "string",
        "description": "string",
        "pain_minute": 0,
        "pain_level": 0,
        "sleep_quality": 0,
        "painful_number": 0,
        "painful_area": "string",
        "item_feel_tag": [],
        "item_foreboding_tag": [],
        "item_triggers_tag": [
            {
                "id": 0
            }
        ],
        "item_complication_tag": [
            {
                "id": 0
            }
        ],
        "item_affect_tag": [
            {
                "id": 0
            }
        ],
        "item_relief_pain_tag": [
            {
                "id": 0
            }
        ],
        "item_drug_tag": [
            {
                "id": 0
            }
        ],
        "item_treatment_tag": [
            {
                "id": 0
            }
        ],
        "item_emotions_tag": [
            {
                "id": 0
            }
        ]
    }
    response = client.post(
        f"{settings.API_V1_STR}/items/", headers=superuser_token_headers, json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == data["title"]
    assert content["description"] == data["description"]
    assert "id" in content
    assert "owner_id" in content


def test_read_item(
        client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    item = create_random_item(db)
    response = client.get(
        f"{settings.API_V1_STR}/items/{item.id}", headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == item.title
    assert content["description"] == item.description
    assert content["id"] == item.id
    assert content["owner_id"] == item.owner_id
