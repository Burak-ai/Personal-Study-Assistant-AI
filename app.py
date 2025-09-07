import pandas as pd
import os
import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt

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
    time_spent = st.number_input("Timespent(In minutes)", min_value=0.0, value=60.0,step=5.0)
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

    total_available = work_hours * 60  # hours to minutes
    st.info(f"You planned {total_available:.0f} minutes of study today.")

st.subheader("Total Study Time per Subject")
time_per_subject = df.groupby("Subject")["TimeSpent"].sum()
st.bar_chart(time_per_subject)

st.subheader("Average Confidence per Subject")
conf_per_subject = df.groupby("Subject")["Confidence"].mean()
st.bar_chart(conf_per_subject)

st.subheader("Study Time Distribution")
plt.clf()
df.groupby("Subject")["TimeSpent"].sum().plot.pie(autopct='%1.0f%%')
st.pyplot(plt.gcf())

st.subheader("Study Progress Over Time")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
time_over_time = df.groupby("Date")["TimeSpent"].sum()
st.line_chart(time_over_time)

today = pd.to_datetime(datetime.now().strftime("%Y-%m-%d"))
actual = df[df["Date"] == today]["TimeSpent"].sum()
planned = work_hours * 60
progress = actual / planned if planned > 0 else 0
st.write(f"Today's progress: {actual:.0f} / {planned:.0f} minutes")
st.progress(progress)

