from typing import Any, Generator, Optional
from sqlalchemy.orm import Session

from sqlalchemy import select, func
from src.products.abc import ABCProductService
from src.products.models import Product
from src.database import get_session
from sqlalchemy.orm import sessionmaker, aliased


class ProductService(ABCProductService):
    def __init__(self, session_maker: sessionmaker[Session]) -> None:
        self.session_maker: sessionmaker[Session] = session_maker

    # TODO: pagination
    def search(
        self,
        name: str | None = None,
        order_by: Optional[str | list[str]] = ["-parse_date", "price"],
    ):
        for db in get_session():
            _q = select(Product)
            _q = _q.add_columns(
                func.rank()
                .over(partition_by=Product.name, order_by=Product.parse_date.desc())
                .label("rnk")
            )

            if name is not None:
                items = name.split(" ")
                filters = [
                    Product.name.contains(i)
                    if not i.startswith("!")
                    else ~Product.name.contains(i)
                    for i in items
                ]
                _q = _q.where(*filters)

            subquery = _q.subquery()
            aliased_prod = aliased(Product, subquery, name="prods", adapt_on_names=True)
            rnk_column = subquery.c.rnk

            q = select(aliased_prod).filter(rnk_column == 1)

            if order_by is not None:
                target_order = (
                    order_by.split() if isinstance(order_by, str) else order_by
                )

                for i in target_order:
                    if i.startswith("-"):
                        q = q.order_by(getattr(aliased_prod, i[1:]).desc())
                    else:
                        q = q.order_by(getattr(aliased_prod, i).asc())

            result = db.execute(q.offset(0).limit(100)).scalars().all()

            return result
