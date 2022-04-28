import pytest
from fastapi.testclient import TestClient

from core.api import app

client = TestClient(app)


def test_top_news_aggregator():
    response = client.get("/news")
    assert response.status_code == 200
    for item in response.json():
        print(item)
        assert item.get("source") in ["newsapi", "reddit"]


@pytest.mark.parametrize("value", ["Johny Depp", "Elon Muusk"])
def test_query_aggregator(value):
    response = client.get(f"/news?{value}")
    assert response.status_code == 200
    for item in response.json():
        print(item)
        assert item.get("source") in ["newsapi", "reddit"]
