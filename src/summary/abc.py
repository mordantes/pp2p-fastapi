from abc import ABC, abstractmethod
from typing import Optional

from pytest import Session
from sqlalchemy.orm import sessionmaker


class ABCSummaryService(ABC):
    @abstractmethod
    def __init__(self, session_maker: sessionmaker[Session]) -> None:
        ...

    @abstractmethod
    def get_recent(
        self,
        *,
        offset: Optional[int] = 0,
        limit: Optional[int] = 50,
        order_by: Optional[str] = "name",
        name: Optional[str] = None
    ):
        """Get recent stat about items"""
