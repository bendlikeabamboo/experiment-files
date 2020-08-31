import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash()

app.layout = html.Div(
    children=[
        html.H1('Start Tutorial'),
        dcc.Graph(
            id='example', 
            figure={
                'data':[
                    {
                        'x':[1,2,3,4,5,],
                        'y':[2,4,6,6,8,],
                        'type':'line',
                        'name':'boats',
                    },
                    {
                        'x':[1,2,3,4,5,],
                        'y':[1,4,6,9,14,],
                        'type':'bar',
                        'name':'yatch',
                    }
                ],
                'layout':{
                    'title':'Basic Dash Example',
                }
            }
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)