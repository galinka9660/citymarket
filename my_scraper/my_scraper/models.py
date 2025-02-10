from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Product(Base):
    __tablename__ = 'parsed_data'
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)