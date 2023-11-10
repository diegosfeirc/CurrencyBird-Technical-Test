from .database import Base

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    transfer_code = Column(String, unique=True, index=True)
    amount = Column(Integer)