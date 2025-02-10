from my_scraper.models import Base, Product
from my_scraper.crud import engine
from sqlalchemy.orm import sessionmaker

Base.metadata.create_all(engine)

def add_product(product):
    product = Product(product_name = product)
    Session = sessionmaker(bind=engine)
    s = Session()
    s.add(product)
    s.commit()
    s.close()

def delete_product():
    pass

def change_product():
    pass

def read_product():
    pass



add_product("IPhone")