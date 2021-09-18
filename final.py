import pandas as pd
import csv
import plotly.graph_objects as py

df = pd.read_csv("mishtu.csv")

student_df=df.loc[df["student_id"]=="TRL_zet"]

print(student_df.groupby("level")["attempt"].mean())

fig = py.Figure(py.Scatter(
    x=student_df.groupby("level")["attempt"].mean(),
    y=["Level 1","Level 2","Level 3","Level 4"],
    orientation="h"))
    
fig.show()