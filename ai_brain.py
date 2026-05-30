# ai_brain.py

import pandas as pd


# ==========================================
# AI INSIGHTS GENERATOR
# ==========================================

def generate_insights(df):

    insights = []

    # --------------------------------------
    # Detect Important Columns Automatically
    # --------------------------------------

    sales_col = next(
        (c for c in df.columns if "sales" in c.lower()),
        None
    )

    profit_col = next(
        (c for c in df.columns if "profit" in c.lower()),
        None
    )

    country_col = next(
        (c for c in df.columns if "country" in c.lower()),
        None
    )

    product_col = next(
        (c for c in df.columns if "product" in c.lower()),
        None
    )

    segment_col = next(
        (c for c in df.columns if "segment" in c.lower()),
        None
    )

    month_col = next(
        (c for c in df.columns if "month" in c.lower()),
        None
    )

    units_col = next(
        (c for c in df.columns if "unit" in c.lower()),
        None
    )

    discount_col = next(
        (c for c in df.columns if "discount" in c.lower()),
        None
    )

    # ==========================================
    # OVERVIEW
    # ==========================================

    insights.append("📊 BUSINESS PERFORMANCE OVERVIEW")

    if sales_col:

        total_sales = df[sales_col].sum()

        insights.append(
            f"💰 Total Sales Generated: ${total_sales:,.2f}"
        )

    if profit_col:

        total_profit = df[profit_col].sum()

        insights.append(
            f"📈 Total Profit Earned: ${total_profit:,.2f}"
        )

    if units_col:

        total_units = df[units_col].sum()

        insights.append(
            f"📦 Total Units Sold: {total_units:,.0f}"
        )

    insights.append(
        f"🧾 Dataset contains {len(df):,} records and {len(df.columns)} columns."
    )

    # ==========================================
    # COUNTRY ANALYSIS
    # ==========================================

    if country_col and sales_col:

        country_sales = (
            df.groupby(country_col)[sales_col]
            .sum()
            .sort_values(ascending=False)
        )

        top_country = country_sales.idxmax()
        top_country_value = country_sales.max()

        low_country = country_sales.idxmin()
        low_country_value = country_sales.min()

        insights.append("")

        insights.append("🌍 COUNTRY ANALYSIS")

        insights.append(
            f"🏆 Highest Sales Country: {top_country} (${top_country_value:,.2f})"
        )

        insights.append(
            f"⚠️ Lowest Sales Country: {low_country} (${low_country_value:,.2f})"
        )

    # ==========================================
    # PRODUCT ANALYSIS
    # ==========================================

    if product_col and sales_col:

        product_sales = (
            df.groupby(product_col)[sales_col]
            .sum()
            .sort_values(ascending=False)
        )

        top_product = product_sales.idxmax()
        top_product_sales = product_sales.max()

        low_product = product_sales.idxmin()
        low_product_sales = product_sales.min()

        insights.append("")

        insights.append("🛒 PRODUCT PERFORMANCE")

        insights.append(
            f"🏆 Best Selling Product: {top_product} (${top_product_sales:,.2f})"
        )

        insights.append(
            f"📉 Lowest Selling Product: {low_product} (${low_product_sales:,.2f})"
        )

    # ==========================================
    # PROFIT ANALYSIS
    # ==========================================

    if product_col and profit_col:

        product_profit = (
            df.groupby(product_col)[profit_col]
            .sum()
            .sort_values(ascending=False)
        )

        top_profit_product = product_profit.idxmax()

        insights.append("")

        insights.append("💹 PROFIT ANALYSIS")

        insights.append(
            f"💰 Most Profitable Product: {top_profit_product}"
        )

        negative_products = product_profit[product_profit < 0]

        if len(negative_products) > 0:

            insights.append(
                f"🚨 {len(negative_products)} products are currently generating losses."
            )

    # ==========================================
    # SEGMENT ANALYSIS
    # ==========================================

    if segment_col and sales_col:

        segment_sales = (
            df.groupby(segment_col)[sales_col]
            .sum()
            .sort_values(ascending=False)
        )

        best_segment = segment_sales.idxmax()

        insights.append("")

        insights.append("📦 SEGMENT ANALYSIS")

        insights.append(
            f"🏆 Best Performing Segment: {best_segment}"
        )

    # ==========================================
    # MONTHLY ANALYSIS
    # ==========================================

    if month_col and sales_col:

        monthly_sales = (
            df.groupby(month_col)[sales_col]
            .sum()
            .sort_values(ascending=False)
        )

        best_month = monthly_sales.idxmax()
        worst_month = monthly_sales.idxmin()

        insights.append("")

        insights.append("📅 SALES TREND ANALYSIS")

        insights.append(
            f"📈 Highest Sales Month: {best_month}"
        )

        insights.append(
            f"📉 Lowest Sales Month: {worst_month}"
        )

    # ==========================================
    # PROFIT MARGIN
    # ==========================================

    if sales_col and profit_col:

        total_sales = df[sales_col].sum()
        total_profit = df[profit_col].sum()

        if total_sales != 0:

            margin = (
                total_profit / total_sales
            ) * 100

            insights.append("")

            insights.append("📊 PROFITABILITY")

            insights.append(
                f"💹 Overall Profit Margin: {margin:.2f}%"
            )

            if margin > 20:

                insights.append(
                    "✅ Business is operating with a healthy profit margin."
                )

            elif margin > 10:

                insights.append(
                    "⚠️ Profit margin is moderate and can be improved."
                )

            else:

                insights.append(
                    "🚨 Profit margin is low. Cost optimization is recommended."
                )

    # ==========================================
    # DISCOUNT ANALYSIS
    # ==========================================

    if discount_col:

        discount_count = (
            df[discount_col]
            .astype(str)
            .value_counts()
        )

        most_discount = discount_count.idxmax()

        insights.append("")

        insights.append("🏷️ DISCOUNT ANALYSIS")

        insights.append(
            f"🎯 Most used discount category: {most_discount}"
        )

    # ==========================================
    # STRATEGIC RECOMMENDATIONS
    # ==========================================

    insights.append("")

    insights.append("🧠 BUSINESS RECOMMENDATIONS")

    insights.append(
        "• Focus marketing investment on high-performing countries."
    )

    insights.append(
        "• Increase inventory for top-selling products."
    )

    insights.append(
        "• Review low-profit products and optimize pricing."
    )

    insights.append(
        "• Improve sales strategies in weak-performing regions."
    )

    insights.append(
        "• Use seasonal sales trends for future forecasting."
    )

    # ==========================================
    # FINAL OUTPUT
    # ==========================================

    final_output = "\n\n".join(insights)

    return final_output


# ==========================================
# AI QUESTION ANSWERING
# ==========================================

def ask_ai(question, df):

    question = question.lower()

    sales_col = next(
        (c for c in df.columns if "sales" in c.lower()),
        None
    )

    profit_col = next(
        (c for c in df.columns if "profit" in c.lower()),
        None
    )

    country_col = next(
        (c for c in df.columns if "country" in c.lower()),
        None
    )

    product_col = next(
        (c for c in df.columns if "product" in c.lower()),
        None
    )

    segment_col = next(
        (c for c in df.columns if "segment" in c.lower()),
        None
    )

    # ==========================================
    # TOTAL SALES
    # ==========================================

    if "total sales" in question:

        total = df[sales_col].sum()

        return f"💰 Total sales is ${total:,.2f}"

    # ==========================================
    # TOTAL PROFIT
    # ==========================================

    elif "total profit" in question:

        total = df[profit_col].sum()

        return f"📈 Total profit is ${total:,.2f}"

    # ==========================================
    # HIGHEST SALES COUNTRY
    # ==========================================

    elif "highest sales country" in question:

        result = (
            df.groupby(country_col)[sales_col]
            .sum()
            .idxmax()
        )

        return f"🌍 Highest sales country is {result}"

    # ==========================================
    # LOWEST SALES PRODUCT
    # ==========================================

    elif (
        "lowest sold product" in question
        or "lowest sales product" in question
    ):

        result = (
            df.groupby(product_col)[sales_col]
            .sum()
            .idxmin()
        )

        return f"📉 Lowest selling product is {result}"

    # ==========================================
    # BEST PRODUCT
    # ==========================================

    elif (
        "best product" in question
        or "top product" in question
    ):

        result = (
            df.groupby(product_col)[sales_col]
            .sum()
            .idxmax()
        )

        return f"🏆 Best selling product is {result}"

    # ==========================================
    # BEST SEGMENT
    # ==========================================

    elif "best segment" in question:

        result = (
            df.groupby(segment_col)[sales_col]
            .sum()
            .idxmax()
        )

        return f"📦 Best performing segment is {result}"

    # ==========================================
    # COUNTRY SEARCH
    # ==========================================

    elif "country" in question and sales_col:

        country_sales = (
            df.groupby(country_col)[sales_col]
            .sum()
            .sort_values(ascending=False)
        )

        return str(country_sales)

    # ==========================================
    # PRODUCT SEARCH
    # ==========================================

    elif "product" in question and sales_col:

        product_sales = (
            df.groupby(product_col)[sales_col]
            .sum()
            .sort_values(ascending=False)
        )

        return str(product_sales)

    # ==========================================
    # DEFAULT
    # ==========================================

    else:

        return "❌ Sorry, I couldn't understand the business question."