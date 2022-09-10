
from sqlalchemy import Column, String, Boolean, Integer
from app.database import Base, engine


class Item(Base):
    __tablename__ = "item"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    status = Column(Boolean, default=True)


Base.metadata.create_all(bind=engine)
