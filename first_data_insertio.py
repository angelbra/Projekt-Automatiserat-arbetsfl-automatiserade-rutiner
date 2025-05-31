from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modeller import Base, Customer, Account

# Skapa en motor och session
engine = create_engine('postgresql+psycopg2://tucgirls:1234@localhost:5431/tucdb')
Session = sessionmaker(bind=engine)
session = Session()

# 👩‍🦰 Lägg till en ny kund
ny_kund = Customer(
    customer="Klara Karlsson",
    address="Lundavägen 45, Lund",
    phone="0709876543",
    personnummer="920202-5678"
)

# 💳 Skapa ett konto åt kunden
nytt_konto = Account(
    account_number="ACC987654",
    customer=ny_kund  # kopplar kontot till kunden
)

# Lägg till och spara
session.add(ny_kund)
session.add(nytt_konto)
session.commit()
print("✅ Ny testkund har lagts till.")

# Stäng session
session.close()
