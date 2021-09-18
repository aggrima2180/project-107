import pandas as pd
import csv
import plotly.graph_objects as py

df = pd.read_csv("mishtu.csv")

print(df.groupby("level")["attempt"].mean())

fig = py.Figure(py.Scatter(
    x=df.groupby("level")["attempt"].mean(),
    y=["Level 1","Level 2","Level 3","Level 4"],
    orientation="h"))
fig.show()