import pandas as pd
import plotly.express as px

# create a plot scatter
df = pd.read_csv("covid_data.csv")
fig = px.scatter(df, x="date", y="cases", color="country", title="COVID-19 Cases")
fig.show()