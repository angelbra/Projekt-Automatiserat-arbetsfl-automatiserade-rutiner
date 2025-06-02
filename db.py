from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modeller import Base

DATABASE_URL = "postgresql+psycopg2://tucgirls:1234@localhost:5431/tucdb"

engine = create_engine(DATABASE_URL)

# session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

## (TUCgirls, lös: 1234, base: tucdb, 5431).
# Function to create tables
def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    try:
        init_db()
        print("✅ data ready.")
    except Exception as e:
        print("❌ Error ", e)
