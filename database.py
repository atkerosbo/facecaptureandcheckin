from settings import Settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the PostgreSQL database URL
db_url = f"postgresql://{Settings.database_username}:{Settings.database_password}@{Settings.database_hostname}:{Settings.database_port}/{Settings.database_name}"

# Create an engine and session
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()
