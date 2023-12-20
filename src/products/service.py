


from typing import Any, Generator, Optional
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.products.abc import ABCProductService
from src.products.models import Product
from src.database import get_session
from sqlalchemy.orm import sessionmaker


class ProductService(ABCProductService):
    def __init__(self, session_maker : sessionmaker[Session]) -> None:
        self.session_maker : sessionmaker[Session] = session_maker


    def search(self, name: str | None):
        
        for db in get_session() :
            if not name :
                return db.query(Product) \
                            .offset(0) \
                            .limit(100) \
                            .all()
                            
            else :
                items = name.split(' ')
                q = select(Product).offset(0).limit(100)
                
                filters = [
                    Product.name.contains(i)
                    if not i.startswith('!')
                    else ~Product.name.contains(i)
                    for i in items
                ]
                q = q.filter(*filters)

                return db.execute(q).scalars().all()


#                 from sqlalchemy.orm import Session
# from sqlalchemy import select
# from src.products.abc import ABCProductService
# from src.products.models import Product
# from sqlalchemy.orm import sessionmaker


# class ProductService(ABCProductService):

#     def __init__(self, session_maker : sessionmaker[Session]) -> None:
#         self.session_maker : sessionmaker[Session] = session_maker

#     def search(self,  name: str | None):
#         with self.session_maker() as db :
#             query = select(Product).limit(10).offset(0)
#             if name is not None:
#                 items = name.split(' ')
#                 filters = [
#                     Product.name.contains(i)
#                     if not i.startswith('!')
#                     else ~Product.name.contains(i)
#                     for i in items
#                 ]
#                 query = query.filter(*filters)
#             data = db.execute(query).all()
#         return data
