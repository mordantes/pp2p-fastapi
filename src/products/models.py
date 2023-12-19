
from src.database import Base
from sqlalchemy import DateTime, Boolean, Column, ForeignKey, Integer, String


class Product(Base):
    __tablename__ = "products"
    
    index = Column(Integer, unique=True, index=False, primary_key=True)
    name = Column(String, unique=False, index=False)
    shop_name = Column(String, unique=False, index=False)
    category = Column(String, unique=False, index=False)
    sub_category = Column(String, unique=False, index=False)
    price = Column(Integer, unique=False, index=False)
    offer = Column(Integer, unique=False, index=False, nullable=True)
    parse_date = Column(DateTime, unique=False)