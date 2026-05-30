# 📊 AI Business Intelligence Platform

An AI-powered Business Intelligence Dashboard built with Python and Streamlit that provides real-time business analytics, forecasting, intelligent insights, voice assistance, and AI-generated visualizations.

---

## 🚀 Features

### 📈 Real-Time Business Dashboard
- Live KPI Monitoring
- Sales Analysis
- Profit Analysis
- Product Performance Tracking
- Country-wise Performance
- Segment Analysis

### 🧠 AI Business Insights
- Automatic Business Recommendations
- Sales Trend Analysis
- Profitability Analysis
- Product Performance Evaluation
- Strategic Decision Support

### 🤖 AI Business Analyst
- Ask business questions in natural language
- AI-generated answers from business data
- Interactive business intelligence assistant

### 🔮 Sales Forecasting
- Future sales prediction
- Trend forecasting
- Data-driven planning

### 📊 AI Generated Visualizations
- Generate charts using natural language prompts
- Dynamic visualization engine

### 🎤 Voice AI Assistant
- Voice-based business queries
- Speech recognition
- Text-to-speech responses

### 🗄️ Real-Time Database Integration
- MySQL Database (XAMPP)
- Live data updates
- Real-time dashboard refresh
- Scalable business data management

---

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend Development |
| Streamlit | Dashboard UI |
| Pandas | Data Processing |
| Plotly | Interactive Charts |
| MySQL | Database |
| SQLAlchemy | Database Connectivity |
| XAMPP | Local Database Server |
| AI Models | Business Intelligence |
| SpeechRecognition | Voice Assistant |
| gTTS / pyttsx3 | Voice Output |

---

## 📂 Project Structure

```text
AI_ANALYST_AGENT/
│
├── app.py
├── ai_brain.py
├── database.py
├── forecast.py
├── llm_ai.py
├── voice_ai.py
├── ai_visuals.py
│
├── requirements.txt
├── README.md
│
└── datasets/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Business-Intelligence-Platform.git

cd AI-Business-Intelligence-Platform
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Setup

Start:

- Apache
- MySQL

Using XAMPP

Open:

```text
http://localhost/phpmyadmin
```

Create Database:

```sql
CREATE DATABASE ai_business_intelligence;
```

Create Table:

```sql
CREATE TABLE sales_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(100),
    product VARCHAR(100),
    segment VARCHAR(100),
    sales FLOAT,
    profit FLOAT,
    units_sold INT,
    month VARCHAR(50),
    discount VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Application will open at:

```text
http://localhost:8501
```

---

## 📊 Dashboard Modules

### KPI Dashboard
- Total Sales
- Total Profit
- Units Sold
- Products
- Countries

### Analytics
- Sales Trends
- Profit by Country
- Product Performance
- Segment Analysis
- Sales vs Profit
- Heatmaps

### AI Features
- AI Insights
- AI Business Analyst
- AI Visual Generator
- Voice Assistant
- Forecasting Engine

---

## 🎯 Business Benefits

- Real-time decision making
- Automated business reporting
- AI-driven recommendations
- Predictive analytics
- Executive-level insights
- Improved operational efficiency

---

## 🔮 Future Enhancements

- Multi-user Authentication
- Cloud Deployment
- Advanced Forecasting Models (LSTM, Prophet)
- Power BI Integration
- ERP Integration
- Automated Email Reports
- Mobile Dashboard
- Generative AI Executive Reports

---

## 👨‍💻 Author

**Partheep**

Aspiring Data Scientist | AI Developer | Business Intelligence Enthusiast

---

## ⭐ Support

If you like this project:

⭐ Star the repository

🍴 Fork the project

🛠️ Contribute to improvements

---

## 📜 License

This project is licensed under the MIT License.
