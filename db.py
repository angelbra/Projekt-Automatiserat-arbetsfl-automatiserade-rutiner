from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "postgresql+psycopg2://akkangell:Angelica.1@localhost:5432/your_database"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

   ##  sqlalchemy.url = postgresql+psycopg2://akkangell:Angelica.1@localhost:5432/your_database