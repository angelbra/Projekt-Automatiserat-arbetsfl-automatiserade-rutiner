from database import SessionLocal, init_db
from models import Customer, Account, Transaction
from datetime import datetime

# Initialize DB (create tables if they don't exist)
init_db()

# Create DB session
db = SessionLocal()

# Add a customer
customer = Customer(
    customer='Angelica Smith',
    address='123 Main St',
    phone='0701234567',
    personnummer='850101-1234'
)

db.add(customer)
db.commit()
db.refresh(customer)

# Add an account
account = Account(account_number='SE1234567890', customer_id=customer.id)
db.add(account)
db.commit()

# Add a transaction
transaction = Transaction(
    transaction_id='TX1001',
    timestamp=datetime.now(),
    amount=100.0,
    currency='SEK',
    sender_account='SE1234567890',
    receiver_account='SE1234567890',
    sender_country='Sweden',
    sender_municipality='Helsingborg',
    receiver_country='Sweden',
    receiver_municipality='Helsingborg',
    transaction_type='internal',
    notes='Test deposit'
)
db.add(transaction)
db.commit()

print("✅ Data inserted successfully")
