# Importing dependencies:

from sqlalchemy import create_engine
from config import db_password, mapbox_token
from dash import Dash, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import pandas.io.sql as sqlio

# Creating the connection string:
db_string = f"postgresql://postgres:{db_password}@127.0.0.1:5432/Airbnb"

# Creating the sqlalchemy engine:
engine = create_engine(db_string)

# Defining the database query:
query = "select * from full_listing"

# Loading in the data using the sqlalchemy engine and query:
df = sqlio.read_sql_query(query,engine)

# Creating district DataFrames
districts = [{'label': district, 'value': district} for district in sorted(df['neighbourhood'].unique())]
# district_01 = df.loc[(df['neighbourhood']== 'District 1')]
# district_02 = df.loc[(df['neighbourhood']== 'District 2')]
# district_03 = df.loc[(df['neighbourhood']== 'District 3')]
# district_04 = df.loc[(df['neighbourhood']== 'District 4')]
# district_05 = df.loc[(df['neighbourhood']== 'District 5')]
# district_06 = df.loc[(df['neighbourhood']== 'District 6')]
# district_07 = df.loc[(df['neighbourhood']== 'District 7')]
# district_08 = df.loc[(df['neighbourhood']== 'District 8')]
# district_09 = df.loc[(df['neighbourhood']== 'District 9')]
# district_10 = df.loc[(df['neighbourhood']== 'District 10')]
# district_11 = df.loc[(df['neighbourhood']== 'District 11')]
# district_12 = df.loc[(df['neighbourhood']== 'District 12')]
# district_13 = df.loc[(df['neighbourhood']== 'District 13')]
# district_14 = df.loc[(df['neighbourhood']== 'District 14')]
# district_15 = df.loc[(df['neighbourhood']== 'District 15')]
# district_16 = df.loc[(df['neighbourhood']== 'District 16')]
# district_17 = df.loc[(df['neighbourhood']== 'District 17')]
# district_18 = df.loc[(df['neighbourhood']== 'District 18')]
# district_19 = df.loc[(df['neighbourhood']== 'District 19')]
# district_20 = df.loc[(df['neighbourhood']== 'District 20')]
# district_21 = df.loc[(df['neighbourhood']== 'District 21')]
# district_22 = df.loc[(df['neighbourhood']== 'District 22')]
# district_23 = df.loc[(df['neighbourhood']== 'District 23')]
# district_24 = df.loc[(df['neighbourhood']== 'District 24')]
# district_25 = df.loc[(df['neighbourhood']== 'District 25')]
# district_26 = df.loc[(df['neighbourhood']== 'District 26')]
# district_27 = df.loc[(df['neighbourhood']== 'District 27')]
# district_28 = df.loc[(df['neighbourhood']== 'District 28')]
# district_29 = df.loc[(df['neighbourhood']== 'District 29')]
# district_30 = df.loc[(df['neighbourhood']== 'District 30')]
# district_31 = df.loc[(df['neighbourhood']== 'District 31')]
# district_32 = df.loc[(df['neighbourhood']== 'District 32')]
# district_33 = df.loc[(df['neighbourhood']== 'District 33')]
# district_34 = df.loc[(df['neighbourhood']== 'District 34')]
# district_35 = df.loc[(df['neighbourhood']== 'District 35')]

# Mapbox:

px.set_mapbox_access_token(mapbox_token)

# Building out Dash components:
app = Dash(__name__, external_stylesheets = [dbc.themes.SLATE])
mytitle = dcc.Markdown(children="# Airbnb Rental Project")
airbnb_map = dcc.Graph(id = 'map', figure={})
dropdown = dcc.Dropdown(id='district_dropdown', options=districts,
value = "District 19",
clearable = False)

# Customizing the Dash app layout

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([mytitle], width=6)
    ], justify='center'),
    dbc.Row([
        dbc.Col([dropdown], width=6)
    ], justify='center'),
    dbc.Row([
        dbc.Col(id='map_col', width=12)
    ]),
], fluid=True)

# Setting up the Callback
@app.callback(
    Output('map_col', 'children'),
    Input('district_dropdown', 'value')
)
def update_map(district):

    df_sub = df[df.neighbourhood == district]

    fig = px.scatter_mapbox(df_sub,
        lat = df_sub['latitude'],
        lon = df_sub['longitude'])
    # if district == "District 1":
    #     fig = px.scatter_mapbox(district_01,
    #         lat = district_01['latitude'],
    #         lon = district_01['longitude'],
    #         color = district_01['beds'])
    #     fig.update_layout(title = 'Airbnb Rentals')
    # elif district == "District 2":
    #     fig = px.scatter_mapbox(district_02,
    #         lat = district_02['latitude'],
    #         lon = district_02['longitude'],
    #         color = district_02['beds'])
    #     fig.update_layout(title = 'Airbnb Rentals')
    # else:
    #     fig = px.scatter_mapbox(district_19,
    #         lat = district_19['latitude'],
    #         lon = district_19['longitude'], 
    #         color = district_19['beds'])
    #     fig.update_layout(title = 'Airbnb Rentals')

    return dcc.Graph(figure=fig)
# Run app
if __name__=='__main__':
    app.run_server(debug=True, port=8054)