from dash.dependencies import Input
from dash.dependencies import Output
import pandas as pd
import sqlite3


## Read data from SQLite using panda and visualize with Dash
def register_callbacks(dashapp):
    @dashapp.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
    def update_graph(selected_dropdown_label):
        dat = sqlite3.connect('ppe.db')
        query = "SELECT * FROM Mask"
        df = pd.read_sql_query(query, dat)
        return {
            'data': [{
                'x': df.authority,
                'y': df.number
            }],
            'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
        }