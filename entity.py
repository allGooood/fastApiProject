from sqlalchemy import Column, String, Integer

from database import Base


class TestEntity(Base):
    __tablename__ = "be_generator"

    seq = Column("seq", Integer, primary_key=True)
    name = Column("name", String)
    location_type = Column("location_type", Integer)
