import sqlalchemy as sa
from sqlalchemy import sessionmaker

engine = sa.create_engine("sqlite:///memory:")

Session = sessionmaker(bind=engine)
session = Session()
