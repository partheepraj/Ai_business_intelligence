import pandas as pd
from sqlalchemy import create_engine, inspect


def create_db_engine(
    user: str = "root",
    password: str = "",
    host: str = "localhost",
    port: int = 3306,
    database: str = "ai_business_intelligence"
):
    """Create a SQLAlchemy engine for a local XAMPP MySQL database."""
    return create_engine(
        f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    )


def get_table_names(engine):
    """Return available tables from the connected database."""
    inspector = inspect(engine)
    return inspector.get_table_names()


def get_data(table_name: str, engine=None, query: str = None, **engine_kwargs):
    """Load a table or custom query from MySQL into a pandas DataFrame."""
    if engine is None:
        engine = create_db_engine(**engine_kwargs)

    if query is None:
        query = f"SELECT * FROM `{table_name}`"

    return pd.read_sql_query(query, engine)
