# Importing dependencies:

from sqlalchemy import create_engine
from config import db_password, mapbox_token
from dash import Dash, dcc, Output, Input, html
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

card_main = dbc.Card(
    [
    dbc.CardBody(
        [
        html.H4("Visualization Parameters", className="card-title"),
        html.H6("Select your options:", className='class-subtitle'),
        dcc.Dropdown(id='district_dropdown', options= districts, value ='District 19', clearable = False, style = {"color": "#000000"})
        ]
    )
    ],
    color = 'dark',
    inverse = 'False',
    outline = 'False')

card_heatmap = dbc.Card(
    [
    dbc.CardBody(
        [
        html.H6("Heatmap of Bedroom Count and Review Score", className="card-title"),
        dcc.Graph(id='heatmap', figure={})
        ]
    )
    ],
    color='secondary',
    inverse=True
)

card_map = dbc.Card(
    [
    dbc.CardBody(
        [
        html.H4("Map of Airbnb Rentals in Nashville", className='card-title'),
        html.H6("Colors correspond with city district", className='class-subtitle'),
        dcc.Graph(id='map', figure={})
        ]
    )
    ],
    color='info',
    inverse=True
)
card_review_scatter = dbc.Card(
    [
    dbc.CardBody(
        [
        html.H6("Heatmap of Bedroom Count and Review Score", className='card-title'),
        dcc.Graph(id='scatter_plot', figure={})
        ]
    )
    ],
    color='secondary',
    inverse=True
)

card_sep_scatter = dbc.Card(
    [
    dbc.CardBody(
        [
        html.H6("September Prices and Number of Reviews", className='card-title'),
        dcc.Graph(id='sep_scatter', figure={})
        ]
    )
    ], 
    color = 'info',
    inverse = True
    )

card_jun_scatter = dbc.Card(
    [
    dbc.CardBody(
        [
        html.H6("June Prices and Number of Reviews", className='card-title'),
        dcc.Graph(id='jun_scatter', figure={})
        ]
    )
    ], 
    color = 'info',
    inverse = True
    )

card_mar_scatter = dbc.Card(
    [
    dbc.CardBody(
        [
        html.H6("March Prices and Number of Reviews", className='card-title'),
        dcc.Graph(id='mar_scatter', figure={})
        ]
    )
    ], 
    color = 'info',
    inverse = True
    )

card_dec_scatter = dbc.Card(
    [
    dbc.CardBody(
        [
        html.H6("December Prices and Number of Reviews", className='card-title'),
        dcc.Graph(id='dec_scatter', figure={})
        ]
    )
    ], 
    color = 'info',
    inverse = True
    )

mytitle = dcc.Markdown(children="# Airbnb Rental Project")

# quarter_scatter = dcc.Graph(id = 'quarter', figure = {})

# Customizing the Dash app layout

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([mytitle], width=6)
    ], justify='center'),
    dbc.Row([
        dbc.Col([card_main], width=3),
        dbc.Col([card_map], width=8)
    ], justify='left'),
    dbc.Row([
        dbc.Col([card_heatmap], width=5),
        dbc.Col([card_review_scatter], width=6)
    ], justify='center'),

    dbc.Row([
        dbc.Col([card_sep_scatter], width = 5),
        dbc.Col([card_jun_scatter], width = 5)
    ], justify = 'center'),
    
    dbc.Row([
        dbc.Col([card_mar_scatter], width = 5),
        dbc.Col([card_dec_scatter], width = 5)
    ], justify = 'center')
], fluid=True)

# Setting up the Callbacks

# Map callback:
@app.callback(
    Output('map', 'figure'),
    Input('district_dropdown', 'value')
)
def update_map(district):

    df_sub = df[df.neighbourhood == district]
    df_sub.reset_index(inplace=True)

    fig = px.scatter_mapbox(df,
        lat = df['latitude'],
        lon = df['longitude'],
        color = df['neighbourhood'],
        hover_data = df_sub[['property_type', 'accommodates', 'bedrooms', 'beds']],
        center = {'lat':df_sub.loc[0].at['latitude'], 'lon':df_sub.loc[0].at['longitude']},
        zoom = 12)
    return fig

# Scatter plot callback:

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

# Heatmap callback:

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

# Review scattters callback:

@app.callback(
    Output('sep_scatter', 'figure'),
    Output('jun_scatter', 'figure'),
    Output('mar_scatter', 'figure'),
    Output('dec_scatter', 'figure'),
    Input('district_dropdown', 'value')
)
def update_quarter(district):
    df_sub2 = df[(df.neighbourhood == district)]

    fig_4 = px.scatter(df_sub2,
    x = df_sub2['sep_price'],
    y = df_sub2['sep_number_of_reviews'])

    fig_5 = px.scatter(df_sub2,
    x = df_sub2['jun_price'],
    y = df_sub2['jun_number_of_reviews'])

    fig_6 = px.scatter(df_sub2,
    x = df_sub2['mar_price'],
    y = df_sub2['mar_number_of_reviews'])

    fig_7 = px.scatter(df_sub2,
    x = df_sub2['dec_price'],
    y = df_sub2['dec_number_of_reviews'])

    return fig_4, fig_5, fig_6, fig_7



# Run app
if __name__=='__main__':
    app.run_server(debug=True, port=8054)