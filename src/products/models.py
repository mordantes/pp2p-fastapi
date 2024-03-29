from src.database import Base
from sqlalchemy import DateTime, Boolean, Column, ForeignKey, Integer, String


class Product(Base):
    __tablename__ = "products"
    name = Column(String, unique=False, index=False, primary_key=True)
    shop_name = Column(String, unique=False, index=False)
    category = Column(String, unique=False, index=False)
    sub_category = Column(String, unique=False, index=False)
    price = Column(Integer, unique=False, index=False)
    offer = Column(Integer, unique=False, index=False, nullable=True)
    parse_date = Column(DateTime, unique=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
