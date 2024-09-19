from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import DeclarativeBase, sessionmaker


engine = create_engine('sqlite:////Py repos/CatRuler/Catruler.db', echo=True)

metadata = MetaData()


class Base(DeclarativeBase):
    pass


Session = sessionmaker(bind=engine)
session = Session()


# pri i3menenii stolbca, ly4she migrirovat' so staroi db na novyu
