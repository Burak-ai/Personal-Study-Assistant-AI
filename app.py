import pandas as pd
import os
import streamlit as st
from datetime import datetime

Study_log = "study_log.csv"
if not os.path.exists(Study_log):
    df = pd.DataFrame(columns=["Date", "Subject", "TimeSpent", "Confidence", "Details"])
    df.to_csv(Study_log, index=False)
else:
    df = pd.read_csv(Study_log)


with st.form("study_form"): 
    work_hours = st.number_input(
        "How many hours can you work today?", min_value=0.0, value=3.0, step=0.5)
    subject = st.text_input("subject")
    time_spent = st.number_input("Timespent", min_value=0.0, value=60.0,step=5.0)
    confidence = st.slider("Confidence (0-100)", 0, 100, 75)
    details = st.text_area("Details (what you practiced)")
    submit = st.form_submit_button("Add Session")



if submit:
    new_entry = pd.DataFrame([{
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Subject": subject,
        "TimeSpent": time_spent,
        "Confidence": confidence,
        "Details": details,
    }])

    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(Study_log, index=False)
    st.success("Study session added successfully!")

st.subheader("Total Study Time per Subject")
time_per_subject = df.groupby("Subject")["TimeSpent"].sum()
st.bar_chart(time_per_subject)


