import pandas as pd
import os
import streamlit as st

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

from datetime import datetime

if submit:
    new_entry = {
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Subject": subject,
        "TimeSpent": time_spent,
        "Confidence": confidence,
        "Details": details,
    }
    df = df.append(new_entry, ignore_index=True)   # add row to DataFrame
    df.to_csv(Study_log, index=False)              # save back to CSV
    st.success("✅ Study session added successfully!")

st.dataframe(df)



