# ==========================================
# AI BUSINESS INTELLIGENCE PLATFORM
# FULL UPDATED app.py
# ==========================================

import streamlit as st
import pandas as pd
import plotly.express as px

from ai_brain import generate_insights
from forecast import generate_forecast
from llm_ai import ask_llm
from voice_ai import listen, speak
from ai_visuals import generate_ai_visual
from database import create_db_engine, get_data, get_table_names
from streamlit_autorefresh import st_autorefresh

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Business Intelligence Platform",
    page_icon="📊",
    layout="wide"
)


# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
    color: white;
}

h1, h2, h3 {
    color: white;
}

[data-testid="stSidebar"] {
    background-color: #1E1E2F;
}

.stMetric {
    background-color: #1E1E2F;
    padding: 15px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# TITLE
# ==========================================

st.title("📊 AI Business Intelligence Platform")

st.write(
    "AI-powered analytics dashboard with forecasting, voice AI, and intelligent visualizations."
)


# ==========================================
# DATA SOURCE SELECTION
# ==========================================

data_source = st.sidebar.radio(
    "Select data source",
    ("Upload File", "MySQL Database")
)

if "db_df" not in st.session_state:
    st.session_state["db_df"] = None

if "db_table" not in st.session_state:
    st.session_state["db_table"] = None

if "db_connection_error" not in st.session_state:
    st.session_state["db_connection_error"] = None

if "db_engine" not in st.session_state:
    st.session_state["db_engine"] = None

if "db_tables" not in st.session_state:
    st.session_state["db_tables"] = []


df = None

if data_source == "Upload File":
    uploaded_file = st.file_uploader(
        "📂 Upload CSV or Excel File",
        type=["csv", "xlsx"]
    )

    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        df.columns = [col.strip() for col in df.columns]

elif data_source == "MySQL Database":
    st.sidebar.markdown("### MySQL / XAMPP Connection")

    db_host = st.sidebar.text_input("Host", "localhost")
    db_port = st.sidebar.number_input("Port", value=3306)
    db_user = st.sidebar.text_input("User", "root")
    db_password = st.sidebar.text_input("Password", type="password")
    db_name = st.sidebar.text_input("Database", "ai_business_intelligence")

    if st.sidebar.button("Connect to MySQL"):
        try:
            engine = create_db_engine(
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port,
                database=db_name
            )
            table_names = get_table_names(engine)
            st.session_state["db_engine"] = engine
            st.session_state["db_tables"] = table_names
            st.session_state["db_connection_error"] = None
            st.success("Connected to database.")

            if not table_names:
                st.info("Connected, but the database contains no tables yet.")
        except Exception as e:
            st.session_state["db_engine"] = None
            st.session_state["db_tables"] = []
            st.session_state["db_connection_error"] = str(e)
            st.error(f"Connection error: {e}")

    if st.session_state.get("db_connection_error"):
        st.warning(st.session_state["db_connection_error"])

    if st.session_state.get("db_tables"):
        db_table = st.sidebar.selectbox(
            "Select Table",
            st.session_state["db_tables"],
            index=0
        )
    else:
        st.sidebar.info("No tables found in the connected database. Enter the exact table name if it exists.")
        db_table = st.sidebar.text_input("Table", "")

    if st.sidebar.button("Load table"):
        try:
            engine = st.session_state.get("db_engine")
            if engine is None:
                engine = create_db_engine(
                    user=db_user,
                    password=db_password,
                    host=db_host,
                    port=db_port,
                    database=db_name
                )
                st.session_state["db_engine"] = engine

            if not db_table:
                raise ValueError("Table name is required.")

            df = get_data(db_table, engine=engine)
            df.columns = [col.strip() for col in df.columns]
            st.session_state["db_df"] = df
            st.session_state["db_table"] = db_table
            st.session_state["db_connection_error"] = None
            st.success(f"Loaded {len(df)} rows from `{db_table}`")
        except Exception as e:
            st.session_state["db_df"] = None
            st.session_state["db_table"] = None
            st.session_state["db_connection_error"] = str(e)
            available = st.session_state.get("db_tables") or []
            if available:
                st.error(
                    f"Database load error: {e}. Available tables: {', '.join(available)}"
                )
            else:
                st.error(f"Database load error: {e}")

    if st.session_state.get("db_df") is not None:
        df = st.session_state.get("db_df")


# ==========================================
# MAIN APPLICATION
# ==========================================

if df is not None:

    filtered_df = df.copy()

    # ==========================================
    # AUTO DETECT COLUMNS
    # ==========================================

    sales_col = None
    profit_col = None
    units_col = None
    country_col = None
    product_col = None
    segment_col = None
    date_col = None
    month_col = None

    for col in filtered_df.columns:

        lower = col.lower()

        if "sales" in lower or "revenue" in lower:
            sales_col = col

        elif "profit" in lower:
            profit_col = col

        elif "unit" in lower:
            units_col = col

        elif "country" in lower:
            country_col = col

        elif "product" in lower:
            product_col = col

        elif "segment" in lower:
            segment_col = col

        elif "date" in lower:
            date_col = col

        elif "month" in lower:
            month_col = col

    # ==========================================
    # SIDEBAR FILTERS
    # ==========================================

    st.sidebar.title("🔎 Filters")

    # COUNTRY FILTER

    if country_col:

        selected_country = st.sidebar.multiselect(
            "Filter Country",
            filtered_df[country_col].dropna().unique()
        )

        if selected_country:

            filtered_df = filtered_df[
                filtered_df[country_col].isin(selected_country)
            ]

    # PRODUCT FILTER

    if product_col:

        selected_product = st.sidebar.multiselect(
            "Filter Product",
            filtered_df[product_col].dropna().unique()
        )

        if selected_product:

            filtered_df = filtered_df[
                filtered_df[product_col].isin(selected_product)
            ]

    # SEGMENT FILTER

    if segment_col:

        selected_segment = st.sidebar.multiselect(
            "Filter Segment",
            filtered_df[segment_col].dropna().unique()
        )

        if selected_segment:

            filtered_df = filtered_df[
                filtered_df[segment_col].isin(selected_segment)
            ]

    # ==========================================
    # DATASET PREVIEW
    # ==========================================

    st.markdown("## 📋 Dataset Preview")

    search = st.text_input(
        "🔍 Search in dataset"
    )

    if search:

        mask = filtered_df.astype(str).apply(
            lambda x: x.str.contains(
                search,
                case=False,
                na=False
            )
        ).any(axis=1)

        filtered_df = filtered_df[mask]

    st.dataframe(
        filtered_df,
        use_container_width=True,
        height=500
    )

    # ==========================================
    # DOWNLOAD FILTERED DATA
    # ==========================================

    csv = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Download Filtered Data",
        csv,
        "filtered_data.csv",
        "text/csv"
    )

    # ==========================================
    # KPI DASHBOARD
    # ==========================================

    st.markdown("## 📊 KPI Dashboard")

    total_sales = (
        filtered_df[sales_col].sum()
        if sales_col else 0
    )

    total_profit = (
        filtered_df[profit_col].sum()
        if profit_col else 0
    )

    total_units = (
        filtered_df[units_col].sum()
        if units_col else 0
    )

    total_countries = (
        filtered_df[country_col].nunique()
        if country_col else 0
    )

    total_products = (
        filtered_df[product_col].nunique()
        if product_col else 0
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "💰 Total Sales",
        f"${total_sales:,.2f}"
    )

    col2.metric(
        "📈 Total Profit",
        f"${total_profit:,.2f}"
    )

    col3.metric(
        "📦 Units Sold",
        f"{total_units:,.0f}"
    )

    col4.metric(
        "🌍 Countries",
        total_countries
    )

    col5.metric(
        "🛍 Products",
        total_products
    )

    # ==========================================
    # SALES TREND
    # ==========================================

    if sales_col and date_col:

        st.markdown("## 📈 Sales Trend Over Time")

        filtered_df[date_col] = pd.to_datetime(
            filtered_df[date_col],
            errors="coerce"
        )

        trend_df = (
            filtered_df.groupby(date_col)[sales_col]
            .sum()
            .reset_index()
        )

        fig = px.line(
            trend_df,
            x=date_col,
            y=sales_col,
            markers=True,
            title="Monthly Sales Trend"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ==========================================
    # PROFIT BY COUNTRY
    # ==========================================

    if profit_col and country_col:

        st.markdown("## 📊 Profit by Country")

        country_profit = (
            filtered_df.groupby(country_col)[profit_col]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            country_profit,
            x=profit_col,
            y=country_col,
            orientation="h",
            title="Country vs Profit"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ==========================================
    # PRODUCT PERFORMANCE
    # ==========================================

    if product_col and sales_col:

        st.markdown("## 🥧 Product Performance")

        product_sales = (
            filtered_df.groupby(product_col)[sales_col]
            .sum()
            .reset_index()
        )

        fig = px.pie(
            product_sales,
            names=product_col,
            values=sales_col,
            title="Product Contribution To Sales"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ==========================================
    # SEGMENT ANALYSIS
    # ==========================================

    if segment_col and product_col and profit_col:

        st.markdown("## 📦 Segment Analysis")

        fig = px.treemap(
            filtered_df,
            path=[segment_col, product_col],
            values=profit_col,
            title="Segment → Product → Profit"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ==========================================
    # SALES VS PROFIT
    # ==========================================

    if sales_col and profit_col:

        st.markdown("## 🔵 Sales vs Profit")

        filtered_df["Bubble_Size"] = (
            filtered_df[profit_col].abs()
        )

        fig = px.scatter(
            filtered_df,
            x=sales_col,
            y=profit_col,
            color=product_col if product_col else None,
            size="Bubble_Size",
            hover_data=filtered_df.columns,
            title="Sales vs Profit Analysis"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ==========================================
    # HEATMAP
    # ==========================================

    if month_col and country_col and sales_col:

        st.markdown("## 🔥 Monthly Heatmap")

        heatmap_df = filtered_df.pivot_table(
            values=sales_col,
            index=country_col,
            columns=month_col,
            aggfunc="sum"
        )

        fig = px.imshow(
            heatmap_df,
            text_auto=True,
            aspect="auto",
            title="Month vs Country vs Sales"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ==========================================
    # TOP PRODUCTS
    # ==========================================

    if product_col and profit_col:

        st.markdown("## 🏆 Top Products")

        top_products = (
            filtered_df.groupby(product_col)[profit_col]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )

        fig = px.bar(
            top_products,
            x=product_col,
            y=profit_col,
            title="Top 10 Products by Profit"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ==========================================
    # AI INSIGHTS
    # ==========================================

    st.markdown("## 🧠 AI Insights")

    try:

        insights = generate_insights(filtered_df)

        st.success(insights)

    except Exception as e:

        st.error(f"Insight Error: {e}")

    # ==========================================
    # AI BUSINESS ANALYST
    # ==========================================

    st.markdown("## 🤖 AI Business Analyst")

    question = st.text_input(
        "Ask business questions"
    )

    if st.button("Ask AI"):

        with st.spinner("AI analyzing data..."):

            try:

                answer = ask_llm(
                    question,
                    filtered_df
                )

                st.success(answer)

            except Exception as e:

                st.error(f"AI Error: {e}")

    # ==========================================
    # AI GENERATED VISUALIZATION
    # ==========================================

    st.markdown("## 🧠 AI Generated Visualization")

    visual_question = st.text_input(
        "Ask AI to generate chart"
    )

    if st.button("Generate AI Chart"):

        fig = generate_ai_visual(
            visual_question,
            filtered_df
        )

        if fig:

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        else:

            st.error(
                "AI could not determine the correct chart."
            )

    # ==========================================
    # VOICE AI ASSISTANT
    # ==========================================

    st.markdown("## 🎤 Voice AI Assistant")

    if st.button("🎙 Start Voice Assistant"):

        st.info("Listening for 5 seconds...")

        user_voice = listen()

        st.success(f"You said: {user_voice}")

        if "error" not in user_voice.lower():

            try:

                answer = ask_llm(
                    user_voice,
                    filtered_df
                )

                st.success(answer)

                speak(answer)

            except Exception as e:

                st.error(f"Voice AI Error: {e}")

        else:

            st.error(user_voice)

    # ==========================================
    # AI SALES FORECAST
    # ==========================================

    st.markdown("## 🔮 AI Sales Forecast")

    forecast_df = generate_forecast(
        filtered_df
    )

    if forecast_df is not None:

        st.dataframe(
            forecast_df,
            use_container_width=True
        )

        fig_forecast = px.line(
            forecast_df,
            x="Future_Period",
            y="Predicted_Sales",
            markers=True,
            title="Future Sales Forecast"
        )

        st.plotly_chart(
            fig_forecast,
            use_container_width=True
        )

    # ==========================================
    # REPORT DOWNLOAD
    # ==========================================

    st.markdown("## 📄 AI Report")

    report = f"""
AI BUSINESS REPORT

Total Sales: ${total_sales:,.2f}
Total Profit: ${total_profit:,.2f}
Units Sold: {total_units:,.0f}
Countries: {total_countries}
Products: {total_products}

Generated by AI Business Intelligence Platform
"""

    st.download_button(
        label="📥 Download Report",
        data=report,
        file_name="AI_Report.txt",
        mime="text/plain"
    )

else:

    if data_source == "Upload File":
        st.info("📂 Upload a dataset to begin.")
    else:
        st.info("🔌 Connect to your XAMPP MySQL database and load a table to begin.")