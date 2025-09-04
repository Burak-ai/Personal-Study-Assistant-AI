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

    subject = st.text_input("subject")
    time_spent = st.number_input("Timespent", min_value=0.0, value=60.0,step=5.0)
    confidence = st.slider("Confidence (0-100)", 0, 100, 75)
    details = st.text_area("Details (what you practiced)")
    submit = st.form_submit_button("Add Session")
