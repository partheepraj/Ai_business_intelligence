import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:@localhost/ai_business_intelligence"
)

df = pd.read_sql(
    "SELECT * FROM sales_data",
    engine
)

print(df)