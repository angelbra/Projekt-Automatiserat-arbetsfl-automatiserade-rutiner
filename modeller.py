from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer = Column(String, nullable=False)
    address = Column(String)
    phone = Column(String)
    personnummer = Column(String, unique=True)

    accounts = relationship('Account', back_populates='customer')

    def __repr__(self):
        return f'<Customer {self.id}: {self.customer}, {self.address}, {self.phone}, {self.personnummer}>'

    def add_account(self, account_number):
        new_account = Account(account_number=account_number, customer_id=self.id)
        self.accounts.append(new_account)
        return new_account


class Account(Base):
    __tablename__ = 'accounts'

    account_number = Column(String, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)

    customer = relationship('Customer', back_populates='accounts')

    sent_transactions = relationship(
        'Transaction',
        foreign_keys='Transaction.sender_account',
        back_populates='sender_account_rel'
    )
    received_transactions = relationship(
        'Transaction',
        foreign_keys='Transaction.receiver_account',
        back_populates='receiver_account_rel'
    )

    def __repr__(self):
        return f'<Account {self.account_number}>'


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    transaction_id = Column(String, unique=True)
    timestamp = Column(DateTime)
    amount = Column(Float, nullable=False)
    currency = Column(String)
    sender_account = Column(String, ForeignKey('accounts.account_number'), nullable=False)
    receiver_account = Column(String, ForeignKey('accounts.account_number'), nullable=False)
    sender_country = Column(String, nullable=True)
    sender_municipality = Column(String, nullable=True)
    receiver_country = Column(String, nullable=True)
    receiver_municipality = Column(String, nullable=True)
    transaction_type = Column(String, nullable=True)
    notes = Column(String, nullable=True)

    sender_account_rel = relationship(
        'Account',
        foreign_keys=[sender_account],
        back_populates='sent_transactions'
    )
    receiver_account_rel = relationship(
        'Account',
        foreign_keys=[receiver_account],
        back_populates='received_transactions'
    )

    def __repr__(self):
        return (f'<Transaction {self.transaction_id}: {self.amount} {self.currency} from '
                f'{self.sender_account} to {self.receiver_account} at {self.timestamp}>')
