from typing import Optional
from fastapi import Depends, routing, Query
from src.products.dependencies import get_service
from src.products.schema import ProductResponseModel, ProductSchema
from src.products.abc import ABCProductService
from src.database import get_session
from src.products.service import ProductService



router = routing.APIRouter(
    prefix='/products',
    tags=['Router for product search']
)

@router.get(
    '/',
    response_model = ProductResponseModel
)
def get_products(
    service : ABCProductService = Depends(get_service),
    q : Optional[str] = Query(None),
):
    try :
        data = service.search(q)
        return {
            'data' : data
        }
    except BaseException as error :
        return { 'msg' : str(error) }




__all__ = [ 
    'router'
]