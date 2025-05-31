from sqlalchemy import create_engine
from modeller import Base  # import

def create_tables():
    
    engine = create_engine('postgresql://tucgirls:1234@localhost:5431/tucdb')

    # table
    Base.metadata.create_all(engine)
    print("✅ Tablas creadas correctamente.")

if __name__ == "__main__":
    create_tables()
