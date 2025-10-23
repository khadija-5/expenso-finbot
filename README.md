# 💰 Expenso FinBot - AI-Powered Expense Tracker

An intelligent personal finance management application built with **Python** and **Streamlit**, featuring an **AI chatbot (FinBot)** for personalized budgeting and financial insights.

*(Optional: Agar aapke paas apne project ka screenshot hai to yahan daal dein)*

---

## ✨ Features

- 📊 **Transaction Tracking:** Track income and expenses with detailed logging.  
- 📈 **Data Visualization:** Dynamic charts (Pie charts, Trend lines) to show spending habits by category and time.  
- 🔒 **User Authentication:** Secure registration and login functionality (SQLite based).  
- 🤖 **FinBot AI Assistant:** Integrated chatbot powered by the **Cohere Chat API** that analyzes your transaction data and provides actionable financial advice, savings suggestions, and budgeting tips.  
- ⚙️ **Multi-Page Interface:** Structured navigation using Streamlit's multi-page architecture.  

---

## 🛠️ Technology Stack

| Component | Technology / Library | Role |
|------------|----------------------|------|
| **Frontend/UI** | Streamlit | Web application framework for easy UI development |
| **Backend/Logic** | Python | Core programming language |
| **AI Assistant** | Cohere (Command-R) | Generative AI for financial analysis (FinBot) |
| **Data Storage** | Pandas, SQLite | Data manipulation and local database for transactions |
| **Visualization** | Plotly | Interactive charts and graphs |

---

## 🚀 Deployment (Streamlit Cloud)

This application is deployed and hosted on **Streamlit Community Cloud**.

**Live Demo:** [Yahan apni deployed Streamlit App ka Link Daal Dein]

---

## 💻 Local Setup (Install & Run)

### 1. Prerequisites
You must have **Python 3.8+** installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/khadija-5/expenso-finbot.git
cd expenso-finbot

### 3. Setup Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Linux/macOS
.\venv\Scripts\activate   # On Windows


---

### 4. Install Dependencies  
Install all required Python packages from the `requirements.txt` file:  

```bash
pip install -r requirements.txt


### 5. Configure API Key  

Create a file named `.env` in the root directory (same place as `home.py`) and add your Cohere API key:  

```bash
# .env file content
COHERE_API_KEY="YOUR_COHERE_API_KEY_HERE"


### 6. Run the Application  

Start the Streamlit application from the root directory:  

```bash
streamlit run home.py

## The application will open in your web browser, typically at:  
👉 [http://localhost:8501](http://localhost:8501)


## 🤝 Contribution  

This project was developed by **Khadija** as a demonstration of an **AI-enhanced application**.  
Feel free to **fork** the repository or suggest **improvements!**



