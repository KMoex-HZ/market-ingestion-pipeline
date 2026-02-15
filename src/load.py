from src.utils import get_db_engine

def load_to_postgres(df, table_name='crypto_prices'):
    """
    Loads a pandas DataFrame into a PostgreSQL database table.
    
    Args:
        df (pd.DataFrame): The source DataFrame containing processed market data.
        table_name (str): The target table name in the database. Defaults to 'crypto_prices'.
    
    Returns:
        None: Data is appended directly to the database.
    """
    # Initialize SQLAlchemy engine from utility module
    engine = get_db_engine()
    
    # Write the DataFrame to the SQL table using 'append' mode
    # index=False ensures the pandas index is not stored as a separate column
    df.to_sql(table_name, engine, if_exists='append', index=False)