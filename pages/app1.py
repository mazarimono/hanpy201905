import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.Div([
        html.H1('自己紹介', style={'textAlign': 'center', 'background': '#EEFFDD', 'marginTop': '3%', 'padding': '1%','fontSize': '400%'}),
            ]),
        html.Div([
            html.Div([
                html.Img(src="https://cdn-ak.f.st-hatena.com/images/fotolife/m/mazarimono/20190315/20190315143003.png",
                style = {'height': '130%'})
            ] , style={'marginTop':'5%', 'marginLeft': '5%', 'display': 'inline-block', 'height': 500}),
            html.Div([
                dcc.Link('hideyan', href='https://twitter.com/OgawaHideyuki', style={'marginBottom': '3%', 'textDecoration':'none'}),
                html.Br(),
                html.Div(' '),
                html.H1('Data VisualizationでPyconjpのトーク応募を計画中。'),
                html.H1('はんなりPython運営'),
                html.H1('合同会社　長目　経営'),
                html.H1('データ分析、金融、ブロックチェーン'),
                html.H1('最近IoTも'),
                html.H1('何事も全力でをモットーに。'),
                
                ], style={'display': 'inline-block', 'fontSize': '300%', 'marginLeft': '5%', 'color': 'limegreen'})
        ], style={'background': '#EEFFDD'}),
    html.Div([    
    dcc.Link('Go to Next Page', href = 'app2'),
    html.Br(),
    dcc.Link('Go to Page1', href = '/')
    ], style = {'textAlign': 'right', 'marginRight': '5%'}),
])