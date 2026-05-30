import plotly.express as px
import pandas as pd


# ==========================================
# AI VISUALIZATION ENGINE
# ==========================================

def generate_ai_visual(question, df):

    question = question.lower()

    columns = df.columns

    sales_col = None
    profit_col = None
    country_col = None
    product_col = None
    date_col = None
    segment_col = None

    # ==========================================
    # DETECT COLUMNS
    # ==========================================

    for col in columns:

        lower = col.lower()

        if "sales" in lower or "revenue" in lower:
            sales_col = col

        elif "profit" in lower:
            profit_col = col

        elif "country" in lower:
            country_col = col

        elif "product" in lower:
            product_col = col

        elif "date" in lower:
            date_col = col

        elif "segment" in lower:
            segment_col = col

    # ==========================================
    # SALES BY COUNTRY
    # ==========================================

    if "country" in question and sales_col and country_col:

        chart_df = (
            df.groupby(country_col)[sales_col]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            chart_df,
            x=country_col,
            y=sales_col,
            title="Sales by Country"
        )

        return fig

    # ==========================================
    # PROFIT BY COUNTRY
    # ==========================================

    elif "profit" in question and "country" in question and profit_col:

        chart_df = (
            df.groupby(country_col)[profit_col]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            chart_df,
            x=country_col,
            y=profit_col,
            title="Profit by Country"
        )

        return fig

    # ==========================================
    # MONTHLY SALES TREND
    # ==========================================

    elif (
        "trend" in question
        or "monthly" in question
        or "time" in question
    ) and date_col and sales_col:

        df[date_col] = pd.to_datetime(
            df[date_col],
            errors="coerce"
        )

        chart_df = (
            df.groupby(date_col)[sales_col]
            .sum()
            .reset_index()
        )

        fig = px.line(
            chart_df,
            x=date_col,
            y=sales_col,
            markers=True,
            title="Sales Trend"
        )

        return fig

    # ==========================================
    # PRODUCT CONTRIBUTION
    # ==========================================

    elif (
        "product" in question
        or "contribution" in question
        or "share" in question
    ) and product_col and sales_col:

        chart_df = (
            df.groupby(product_col)[sales_col]
            .sum()
            .reset_index()
        )

        fig = px.pie(
            chart_df,
            names=product_col,
            values=sales_col,
            title="Product Contribution"
        )

        return fig

    # ==========================================
    # SEGMENT ANALYSIS
    # ==========================================

    elif (
        "segment" in question
    ) and segment_col and sales_col:

        chart_df = (
            df.groupby(segment_col)[sales_col]
            .sum()
            .reset_index()
        )

        fig = px.treemap(
            chart_df,
            path=[segment_col],
            values=sales_col,
            title="Segment Analysis"
        )

        return fig

    # ==========================================
    # SALES VS PROFIT
    # ==========================================

    elif (
        "sales vs profit" in question
        or "scatter" in question
    ) and sales_col and profit_col:

        fig = px.scatter(
            df,
            x=sales_col,
            y=profit_col,
            color=product_col if product_col else None,
            title="Sales vs Profit"
        )

        return fig

    return None