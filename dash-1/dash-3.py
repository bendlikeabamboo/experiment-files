import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_html_components as html
import plotly.express as px
import pandas as pd
import pandas_datareader.data as web
import datetime



app = dash.Dash()

app.layout = html.Div(
    children=[
        html.Div(children='''Symbol to graph'''),
        dcc.Input(id='input', value='', type='text'),
        html.Div(id='output-graph'),
    ]
)


@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)

def update_graph(input_data):
    start = datetime.datetime(2020, 5, 5)
    end = datetime.datetime.now()
    df = web.DataReader(input_data, 'yahoo', start, end)
    graph = dcc.Graph(
        id='example', 
        figure={
            'data':[
                {
                    'x':df.index,
                    'y':df['Close'],
                    'type':'line',
                    'name':input_data,
                },
            ],
            'layout':{
                'title':input_data,
            }
        }
    )
    return graph

if __name__ == '__main__':
    app.run_server(debug=True)