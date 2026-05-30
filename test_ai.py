import pandas as pd
from sqlalchemy import create_engine
from ai_brain import generate_insights

engine = create_engine(
    "mysql+pymysql://root:@localhost/ai_business_intelligence"
)

df = pd.read_sql(
    "SELECT * FROM sales_data",
    engine
)

print(generate_insights(df))