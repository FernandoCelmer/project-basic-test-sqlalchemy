from app.database import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Item


SQLALCHEMY_DATABASE_TEST_URL = "sqlite:///./sql_app_test.db"

engine = create_engine(
    url=SQLALCHEMY_DATABASE_TEST_URL,
    connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)