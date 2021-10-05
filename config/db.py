from sqlalchemy import create_engine, MetaData
from sqlalchemy.sql.schema import MetaData

engine = create_engine("mysql+pymysql://root:secret@localhost:3306/test")
meta = MetaData()
conn =  engine.connect()