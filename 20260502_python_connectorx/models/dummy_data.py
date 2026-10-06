from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Float, DateTime
from config.config import config

class Base(DeclarativeBase):
    pass

class DummyData(Base):
    __tablename__ = config["db"]["table"]
    id          :Mapped[int]    = mapped_column(Integer, primary_key=True, autoincrement=True)
    name        :Mapped[str]    = mapped_column(String(50), nullable=True)
    email       :Mapped[str]    = mapped_column(String(50), nullable=True)
    age         :Mapped[int]    = mapped_column(Integer, nullable=True)
    country     :Mapped[str]    = mapped_column(String(2), nullable=True)
    score       :Mapped[float]  = mapped_column(Float, nullable=True)
    created_at  :Mapped[str]    = mapped_column(DateTime, nullable=False)