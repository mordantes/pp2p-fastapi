
from src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_products_list():
    response = client.get("/products")
    print(response)
    assert response.status_code == 200