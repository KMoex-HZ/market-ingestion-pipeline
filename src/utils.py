import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db_engine():
    """
    Creates and returns a SQLAlchemy database engine.
    Fetches database credentials from environment variables for security.
    
    Returns:
        sqlalchemy.engine.Engine: Database connection engine.
    """
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    db = os.getenv('DB_NAME')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    
    # We use 'db' as the host because within the Docker network, 
    # the PostgreSQL service is identified by its service name 'db'.
    connection_string = f'postgresql://{user}:{password}@db:{port}/{db}'
    
    return create_engine(connection_string)