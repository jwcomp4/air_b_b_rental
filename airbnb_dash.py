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

# Mapbox:

px.set_mapbox_access_token(mapbox_token)

# Building out Dash components:
app = Dash(__name__, external_stylesheets = [dbc.themes.SLATE])
mytitle = dcc.Markdown(children="# Airbnb Rental Project")
airbnb_map = dcc.Graph(id = 'map', figure={})
price_rev_scatter = dcc.Graph(id = 'scatter_plot', figure ={})
bedroom_heatmap = dcc.Graph(id = 'heatmap', figure = {})
quarter_scatter = dcc.Graph(id = 'quarter', figure = {})
dropdown = dcc.Dropdown(id='district_dropdown', options=districts,
value = "District 19",
clearable = False)
quarter_dropdown = dcc.Dropdown(id='quarter_drop', options = df.columns[10:14],
value = 'sep_price')

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
    dbc.Row([
        dbc.Col([price_rev_scatter], width=12)
    ], justify='center'), 
    dbc.Row([
        dbc.Col([bedroom_heatmap], width=12)
    ], justify='center'),
    dbc.Row([
        dbc.Col([quarter_dropdown], width = 12)
    ], justify = 'center'),
    dbc.Row([
        dbc.Col([quarter_scatter], width = 12)
    ], justify = 'center')
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

@app.callback(
    Output('scatter_plot', 'figure'),
    Input('district_dropdown', 'value')
)
def update_scatter(district):
    df_sub = df[df.neighbourhood == district]

    fig_2 = px.scatter(df_sub,
        x = df_sub['review_scores_rating'],
        y = df_sub['sep_price'],
        labels ={'review_scores_rating':'Review Score', 'sep_price':'Price' },
        color = df_sub['property_type'],
        symbol = df_sub['property_type'],
        hover_data = ['sep_price', 'review_scores_rating', 'bedrooms']
    )

    fig_2.update_layout(title="Price and Review Score Comparison")
    return fig_2

@app.callback(
    Output('heatmap', 'figure'),
    Input('district_dropdown', 'value')
)
def update_heatmap(district):
    df_sub = df[df.neighbourhood == district] 

    fig_3 = px.density_heatmap(df_sub, 
    x = 'bedrooms',
    y = 'review_scores_rating',
    text_auto=True,
    labels = {'review_scores_rating':'Review', 'bedrooms': 'Bedrooms'})

    return fig_3

# @app.callback(
#     Output('quarter', 'figure'),
#     Input('district_dropdown', 'value'),
#     Input('quarter_drop', 'value')
# )
# def update_quarter(district, quarter):
#     df_sub = df[(df.neighbourhood == district] 

# Run app
if __name__=='__main__':
    app.run_server(debug=True, port=8054)