import datetime

from sqlalchemy import Column, DateTime, Integer, Float, MetaData
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.declarative import declarative_base


class Base(object):
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        nullable=False,
    )


DeclarativeBase = declarative_base(cls=Base, metadata=MetaData(schema="rekognizer"))


class Enrollment(DeclarativeBase):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    embedding = Column(postgresql.ARRAY(Float()), nullable=False)
