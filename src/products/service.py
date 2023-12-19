


from typing import Any, Generator, Optional
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.products.abc import ABCProductService
from src.products.models import Product
from src.database import get_session

class ProductService(ABCProductService):

    def __init__(self) -> None:
        super().__init__()

    def get_all(self, name: str | None):
        # query = select(Product).limit(10)
        for db in get_session() :
            if not name :
                return db.query(Product) \
                            .offset(0) \
                            .limit(100) \
                            .all()
                            
            else :
                items = name.split(' ')
                q = db.query(Product)
                
                filters = [
                    Product.name.contains(i)
                    if not i.startswith('!')
                    else ~Product.name.contains(i)
                    for i in items
                ]
                q = q.filter(*filters)

                return q.offset(0).limit(100).all()