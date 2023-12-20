
from src.database import Base
from sqlalchemy import DateTime, Boolean, Column, ForeignKey, Integer, String, Float

from src.summary.schema import SummarySchema


class Summary(Base):
    __tablename__ = "prod_analyze"
    
    name = Column(String, unique=True, index=False, primary_key=True)
    shop_name = Column(String, unique=False, index=False)
    first_date = Column(DateTime, unique=False, nullable=True)
    last_date  = Column(DateTime, unique=False, nullable=True)
    first_value = Column(Integer, unique=False, index=False, nullable=True)
    last_value = Column(Integer, unique=False, index=False, nullable=True)
    min_price = Column(Integer, unique=False, index=False, nullable=True)
    max_price = Column(Integer, unique=False, index=False, nullable=True)
    avg_price = Column(Integer, unique=False, index=False, nullable=True)
    min_offer = Column(Integer, unique=False, index=False, nullable=True)
    records = Column(Integer, unique=False, index=False)
    percent = Column(Float, unique=False, index=False, nullable=True)


    def to_read_model(self, instance):
        return SummarySchema(**instance)