from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class RepositoryScan(Base):
    __tablename__ = 'repository_scans'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    repository_url: Mapped[str] = mapped_column(String(500), index=True)
    summary: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
