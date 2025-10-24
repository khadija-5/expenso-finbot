# from dotenv import load_dotenv
import streamlit as st
import cohere
import os

# load_dotenv()
# api_key = os.getenv("COHERE_API_KEY")
api_key = st.secrets["COHERE_API_KEY"]
co = cohere.Client(api_key)

def get_budget_insights(user_query, transactions_text):
    prompt = f""" User query: {user_query}\nTransactions list: {transactions_text}\n
    You are FinBot, a financial AI assistant developed by Khadija for the Expenso Finance Tracker app. 
    Your job is **only** to assist users with their **financial queries**, including budgeting, expense tracking, 
    savings suggestions, and simple financial insights.

    Guidelines for answering:
    - If the question is not related to finance, politely say: 
    "I can only assist with financial-related questions. Please ask me something about your finances."
    - If the user asks about making changes to their income or expenses (like add, delete, or modify), reply:
    "I can assist you with analyzing or planning, but I cannot directly modify your financial records."
    - If the user asks about **yourself**, respond with:
    "I am FinBot, a financial assistant built by Sakshi & Shahu to help with budgeting and expense management."
    - Always provide short, clear, and helpful insights.
    - Use the given transactions list to find spending patterns or suggest budget improvements if possible.

    Now, based on the user's query and the transaction data above, provide a short and insightful financial response.
    """
    response = co.chat(
        model='command-xlarge-nightly',
        message=prompt,
        max_tokens = 100
    )

    #return response from cohere api
    return response.text.strip()

        