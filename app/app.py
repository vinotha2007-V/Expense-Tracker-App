import streamlit as st
import pandas as pd

st.title("💸 Expense Tracker App")

uploaded_file = st.file_uploader("Upload Expense CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

    st.subheader("Expense Trend")
    st.line_chart(df['Amount'])

    st.subheader("Category-wise Expense")
    st.bar_chart(df.groupby('Category')['Amount'].sum())
