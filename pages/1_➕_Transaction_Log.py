import streamlit as st
from utils.ExpenseTracker import Account
import time

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please log in to continue :)")
    st.stop()

user_email = st.session_state.user_email
db_name = f"{user_email}.db"
account = Account(db_name=db_name)

st.title("💵 Log Transactions")
st.divider()
if "balance" not in st.session_state:
    st.session_state.balance = account.getBalance()

formatted_balance = f"${st.session_state.balance:.2f}"
st.write(f"Current Balance: {formatted_balance}")


#Add Expense
with st.expander("Add New Expense"):
    with st.form("expense_form"):
        exName = st.text_input("Expense Title")
        exDate = st.date_input("Date Of Expense")
        exAmount = st.number_input("Amount Spent", min_value=0.0)
        exDes = st.text_area("Description")
        exCategory = st.selectbox("Category of expense", ("-", "Food 🍕", "Personal 👱🏽", "Transport 🚌", "Investment 🤑"))
        submit_expense = st.form_submit_button("Add Expense ➕")

        if submit_expense:
            account.addExpense(exName, exDate, exAmount, exDes, exCategory)
            st.session_state.balance -= exAmount #deduct from balance
            st.toast("✅ Expense Added Successfully!")
            time.sleep(1.5)
            st.rerun()


#Add Income
with st.expander("Add New Income"):
    with st.form("income_form"):
        inName = st.text_input("Income Title")
        inDate = st.date_input("Date of Income")
        inAmount = st.number_input("Amount Received", min_value = 0.0)
        inDes = st.text_area("Description")
        inSource = st.selectbox("Source of Income", ("-", "Salary 💳", "Family 👪", "Investment 💲", "Other"))
        submit_income = st.form_submit_button("Add Income ➕")

        if submit_income:
            account.addIncome(inName, inDate, inAmount, inDes, inSource)
            st.session_state.balance += inAmount
            time.sleep(1.5)
            st.rerun()
