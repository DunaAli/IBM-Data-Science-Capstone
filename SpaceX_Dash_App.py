# pip install dash plotly pandas
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
df = pd.read_csv("dataset_part_2.csv")
df["Landing"] = df["Class"].map({0:"Not successful", 1:"Successful"})
app = Dash(__name__)
app.layout = html.Div([html.H1("SpaceX Falcon 9 Landing Dashboard"),
 dcc.Dropdown(id="site", options=[{"label":"All Sites","value":"ALL"}]+[{"label":s,"value":s} for s in sorted(df.LaunchSite.unique())],value="ALL"),
 dcc.Graph(id="pie"), dcc.Graph(id="scatter")])
@app.callback(Output("pie","figure"),Output("scatter","figure"),Input("site","value"))
def update(site):
 data = df if site == "ALL" else df[df.LaunchSite == site]
 pie = px.pie(data,names="Landing",title="Landing outcomes by selected site")
 scatter = px.scatter(data,x="PayloadMass",y="Class",color="LaunchSite",hover_data=["Orbit","FlightNumber"],title="Payload mass vs landing outcome")
 return pie,scatter
if __name__ == "__main__": app.run(debug=True)
