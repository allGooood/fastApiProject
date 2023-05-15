from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from setting import config
from urllib.parse import quote

engine = create_engine(f"mysql+pymysql://{config.DATABASE_USERNAME}:{quote(config.DATABASE_PASSWORD, safe='')}"
                       f"@{config.DATABASE_HOST}:{config.DATABASE_PORT}/OPEN_SERVICE")

session_maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = session_maker()
    try:
        yield db
    finally:
        db.close()
