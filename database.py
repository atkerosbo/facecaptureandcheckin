from settings import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the PostgreSQL database URL
db_url = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

# Create an engine and session
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()
