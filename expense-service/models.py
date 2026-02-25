from sqlalchemy import Column, Integer, String, Float
from database import Base

class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True)
    email = Column(String(100))
    title = Column(String(100))
    amount = Column(Float)