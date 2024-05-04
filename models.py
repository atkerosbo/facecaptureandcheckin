from sqlalchemy import TIMESTAMP, Column, Integer, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import text

Base = declarative_base()

class FaceModel(Base):
    __tablename__ = 'faces'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    encoding = Column(LargeBinary)

class Checkin(Base):
    __tablename__ = 'check_ins'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    encoding = Column(LargeBinary)
    timestamp_created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    
