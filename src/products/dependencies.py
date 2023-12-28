from src.products.service import ProductService
from src.database import session_maker


def get_service():
    return ProductService(session_maker)
