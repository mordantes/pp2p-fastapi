from src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


############################# products #############################
def test_products_list():
    response = client.get("/products")
    print(response)
    assert response.status_code == 200


def test_products_list_search():
    response = client.get("/products?q=шоколад")
    print(response)
    assert response.status_code == 200


############################# summary #############################


def test_summary_main():
    response = client.get("/summary")
    print(response)
    assert response.status_code == 200
