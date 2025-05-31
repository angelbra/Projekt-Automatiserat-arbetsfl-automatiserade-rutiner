from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modeller import Base

DATABASE_URL = "postgresql+psycopg2://akkangell:Angelica.1@localhost:5432/your_database"

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
        print("✅ Tablas creadas correctamente en la base de datos.")
    except Exception as e:
        print("❌ Error al crear las tablas:", e)
