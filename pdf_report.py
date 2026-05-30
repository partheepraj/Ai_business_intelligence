from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

# ============================================
# CREATE PDF REPORT
# ============================================

def create_pdf_report(
    total_sales,
    total_profit,
    top_country,
    top_product,
    insights,
    chart_paths
):

    pdf_file = "AI_Business_Report.pdf"

    doc = SimpleDocTemplate(
        pdf_file,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    elements = []

    # ============================================
    # TITLE
    # ============================================

    title = Paragraph(
        "AI Business Intelligence Report",
        styles["Title"]
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    # ============================================
    # KPI SUMMARY
    # ============================================

    summary = f"""
    <b>Total Sales:</b> ${total_sales:,.0f}<br/><br/>
    <b>Total Profit:</b> ${total_profit:,.0f}<br/><br/>
    <b>Top Country:</b> {top_country}<br/><br/>
    <b>Top Product:</b> {top_product}<br/><br/>
    """

    summary_para = Paragraph(
        summary,
        styles["BodyText"]
    )

    elements.append(summary_para)

    elements.append(Spacer(1, 20))

    # ============================================
    # AI INSIGHTS
    # ============================================

    insights_title = Paragraph(
        "AI Insights",
        styles["Heading2"]
    )

    elements.append(insights_title)

    insights_para = Paragraph(
        insights.replace("\n", "<br/>"),
        styles["BodyText"]
    )

    elements.append(insights_para)

    elements.append(Spacer(1, 20))

    # ============================================
    # ADD CHARTS
    # ============================================

    chart_title = Paragraph(
        "Business Visualizations",
        styles["Heading2"]
    )

    elements.append(chart_title)

    elements.append(Spacer(1, 20))

    for chart in chart_paths:

        img = Image(
            chart,
            width=500,
            height=300
        )

        elements.append(img)

        elements.append(Spacer(1, 20))

    # ============================================
    # BUILD PDF
    # ============================================

    doc.build(elements)

    return pdf_file