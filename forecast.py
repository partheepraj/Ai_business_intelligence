import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def generate_forecast(df):

    # Detect sales column
    sales_col = None

    possible_sales = [
        "Sales",
        "sales",
        "Revenue",
        "revenue",
        "Amount"
    ]

    for col in possible_sales:
        if col in df.columns:
            sales_col = col
            break

    if sales_col is None:
        return None

    # Create time index
    df = df.copy()

    df = df.reset_index(drop=True)

    df["Time_Index"] = np.arange(len(df))

    X = df[["Time_Index"]]

    y = df[sales_col]

    # Train model
    model = LinearRegression()

    model.fit(X, y)

    # Predict future
    future_days = 12

    future_index = np.arange(
        len(df),
        len(df) + future_days
    ).reshape(-1, 1)

    predictions = model.predict(future_index)

    forecast_df = pd.DataFrame({
        "Future_Period": np.arange(1, future_days + 1),
        "Predicted_Sales": predictions
    })

    return forecast_df