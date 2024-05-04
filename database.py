# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the PostgreSQL database URL
db_url = 'postgresql://postgres:Komsrv999@localhost:5432/face_rec'

# Create an engine and session
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()
