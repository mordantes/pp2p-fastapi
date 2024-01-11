from itertools import chain
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.summary.abc import ABCSummaryService
from src.summary.models import Summary
from sqlalchemy.orm import sessionmaker


class SummaryService(ABCSummaryService):
    def __init__(self, session_maker: sessionmaker[Session]) -> None:
        self.session_maker: sessionmaker[Session] = session_maker

    def get_recent(
        self,
        *,
        offset: Optional[int] = 0,
        limit: Optional[int] = 10,
        order_by: Optional[str | list[str]] = ["-last_date"],
        name: Optional[str] = None
    ):
        with self.session_maker() as db:
            query = select(Summary)

            if name is not None:
                items = name.split(" ")
                filters = [
                    Summary.name.icontains(i)
                    if not i.startswith("!")
                    else ~Summary.name.icontains(i)
                    for i in items
                ]
                query = query.filter(*filters)

            query = query.limit(limit).offset(offset)
            if order_by is not None:
                target_order = (
                    order_by.split() if isinstance(order_by, str) else order_by
                )
                # print(target_order)
                for i in target_order:
                    if i.startswith("-"):
                        query = query.order_by(getattr(Summary, i[1:]).desc())
                    else:
                        query = query.order_by(getattr(Summary, i).asc())
            data = db.execute(query).scalars().all()

        return data
