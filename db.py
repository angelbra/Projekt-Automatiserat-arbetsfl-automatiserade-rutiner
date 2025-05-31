from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modeller import Base



DATABASE_URL = "postgresql+psycopg2://akkangell:Angelica.1@localhost:5432/your_database"


engine = create_engine(DATABASE_URL)

# session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#  (create tables)
def init_db():
    Base.metadata.create_all(bind=engine)
