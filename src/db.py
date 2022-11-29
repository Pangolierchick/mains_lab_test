import sqlalchemy

engine = sqlalchemy.create_engine("sqlite:///bills.db")
metadata = sqlalchemy.MetaData()

bills = sqlalchemy.Table(
    'bills',
    metadata,
    sqlalchemy.Column('client_name', sqlalchemy.String, primary_key=True),
    sqlalchemy.Column('client_org', sqlalchemy.String, primary_key=True),
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('sum', sqlalchemy.Float),
    sqlalchemy.Column('date', sqlalchemy.String),
    sqlalchemy.Column('service', sqlalchemy.String),
)

metadata.create_all(engine)
