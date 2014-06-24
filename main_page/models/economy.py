from .meta import *


class Wallet(Base):
    __tablename__ = 'wallet'
    id = Column(Integer, primary_key=True)
    balance = Column(Integer)

    def __init__(self, balance):
        self.balance = balance


class Transactions(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    first_wallet_id = Column(Integer, ForeignKey('wallet.id'))
    first_wallet = relationship("Wallet", foreign_keys=[first_wallet_id])
    second_wallet_id = Column(Integer, ForeignKey('wallet.id'))
    second_wallet = relationship("Wallet", foreign_keys=[second_wallet_id])
    amount = Column(Integer)
    title = Column(Text)
    date = Column(DateTime)

    def __init__(self, first_wallet_id, second_wallet_id, amount, title, date):
        self.first_wallet_id = first_wallet_id
        self.second_wallet_id = second_wallet_id
        self.amount = amount
        self.title = title
        self.date = date


class Payments(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True)
    wallet_id = Column(Integer, ForeignKey('wallet.id'))
    wallet = relationship("Wallet")
    amount = Column(Integer)
    name = Column(Text)
    title = Column(Text)
    date = Column(DateTime)

    def __init__(self, first_wallet_id, second_wallet_id, amount, title, date):
        self.first_wallet_id = first_wallet_id
        self.second_wallet_id = second_wallet_id
        self.amount = amount
        self.title = title
        self.date = date

#class Likes(Base):
#	__tablename__ = 'likes'