from typing import Optional
from fastapi import Depends, routing, Query
from src.products.schema import ProductResponseModel, ProductSchema
from src.products.abc import ABCProductService
from src.database import get_session
from src.products.service import ProductService



router = routing.APIRouter(
    prefix='/products',
    tags=['Router for product search']
)

def get_service():
    return ProductService()

@router.get(
    '/',
    response_model= ProductResponseModel
)
def get_products(
    db : ABCProductService = Depends(get_service),
    q : Optional[str] = Query(None),
):
    data = db.get_all(q)
    return {
        'data' : data
    }



__all__ = [ 
    'router'
]