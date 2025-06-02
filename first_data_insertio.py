# first_data_insertion.py
from sqlalchemy.orm import sessionmaker
from modeller import Base, Customer, Account
from db import engine  # importera din databasanslutning

Session = sessionmaker(bind=engine)

def insert_initial_data():
    session = Session()

    # Kontrollera om kunden redan finns för att undvika fel
    befintlig_kund = session.query(Customer).filter_by(personnummer="920202-5678").first()
    if befintlig_kund:
        print("Kunden finns redan, inga data läggs till.")
        session.close()
        return

    ny_kund = Customer(
        customer="Antonio pynochen",
        address="stornygata 12, Malmö",
        phone="12340998778",
        personnummer="941102-5598"
    )
    nytt_konto = Account(
        account_number="ACHY87654",
        customer=ny_kund
    )

    session.add(ny_kund)
    session.add(nytt_konto)
    session.commit()
    session.close()
    print("✅ Ny testkund har lagts till.")
