import streamlit as st
Study_log = "study_log.csv"
headers = ["Date", "Subject", "TimeSpent", "Confidence", "Details"]

with st.form("study_form"): 
    work_hours = st.number_input(
        "How many hours can you work today?",
        min_value=0.0,
        value=3.0,
        step=0.5
)
