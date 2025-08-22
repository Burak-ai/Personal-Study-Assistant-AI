import csv
from datetime import datetime
import os
import pandas as pd 
import matplotlib as plt


Study_log = "study_log.csv"
headers = ["Date", "Subject", "TimeSpent", "Confidence", "Mood", "Details"]

if not os.path.exists(Study_log):
    with open(Study_log, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)


date = datetime.now().strftime("%Y-%m-%d")
subject = input("Subject: ")
time_spent = input("Time spent (minutes): ")
confidence = input("How confident do you feel in this session? (0-100): ")
mood = input("Mood (optional): ")
details = input("Details (what you practiced): ")


with open(Study_log, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([date, subject, time_spent, confidence, mood, details])

print("Study session added successfully! ")

df = pd.read_csv(Study_log)
df["TimeSpent"] = pd.to_numeric(df["TimeSpent"], errors="coerce")
df["Score"] = pd.to_numeric(df["Confidence"], errors="coerce")

# Total study time per subject
df.groupby("Subject")["TimeSpent"].sum().plot(kind="bar")
plt.title("Total Study Time per Subject")
plt.ylabel("Minutes")
plt.show()

# Average score per subject
if not df.empty and df["TimeSpent"].notna().any():
    df.groupby("Subject")["TimeSpent"].sum().plot(kind="bar")
    plt.title("Total Study Time per Subject")
    plt.ylabel("Minutes")
    plt.show()

# Plot average confidence per subject
if not df.empty and df["Confidence"].notna().any():
    df.groupby("Subject")["Confidence"].mean().plot(kind="bar", color="orange")
    plt.title("Average Confidence per Subject")
    plt.ylabel("Confidence (0-100)")
    plt.show()


