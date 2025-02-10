from sqlalchemy import create_engine
from my_scraper.config import DATABASE_URL

engine = create_engine(DATABASE_URL)