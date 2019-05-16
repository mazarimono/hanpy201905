import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.Div([
        html.H1('今日のお題', style={'textAlign': 'center', 'background': '#EEFFDD', 'marginTop': '3%', 'padding': '1%','fontSize': '400%', 'borderRadius':'5%'}),
            ]),
    html.Div([
        html.H2('1. Dashとは？', style = {'margin': '3%'}),
        html.H2('2. 新機能', style = {'marginTop': '5%'} ),
        html.H3('・　Dash-Cytoscape, Dash-DAQ, Dash-Canvas, Dash-Bio', style={'marginBottom': '5%'}),
        html.H2('3. TIPS', style={'marginTop': '5%'}),
        html.H3('・　Dashにない再生ボタンを作るには？'),
        html.H3('・　ファイルを分けて作成しよう',style={'marginBottom': '3%'}),
    ], style={'textAlign': 'center', 'margin': '3%', 'padding':'3%', 'fontSize': '300%', 'background':'#EEFFDD', 'borderRadius': '5%'}),
    html.Div([
        dcc.Link('go to next page', href='app3'),
        html.Br(),
        dcc.Link('go back', href='app1'),
        html.Br(),
        dcc.Link('Back to Top', href='/'),
    ], style = {'textAlign': 'right', 'marginRight': '5%'})
])