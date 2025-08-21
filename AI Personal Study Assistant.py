import csv
from datetime import datetime
import os
import pandas as pd 

df = pd.read_csv("study_log.csv") 
print(df.head())