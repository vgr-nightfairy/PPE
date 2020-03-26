import dash_core_components as dcc
import dash_html_components as html


## Dash configuration of graph
layout = html.Div([
    html.H1('N95 Mask Supply'),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Hospital 1', 'value': 'Hospital 1'},
            {'label': 'Hospital 2', 'value': 'Hospital 2'},
            {'label': 'Hospital 3', 'value': 'Hospital 3'}
        ],
        value='hos'
    ),
    dcc.Graph(id='my-graph'),
], style={'width': '500'})

