import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output 

from app import app 
from pages import app1, app2 

app.layout = html.Div([
        dcc.Location(id = 'url',refresh=False),
        html.Div(id = 'page-content')
])

indexPage = html.Div([
    html.Hr(style={'height': '5%', 'backgroundColor': 'limegreen'}),
    html.H3('はんなりPython #17 令和最初の発表会'),
    html.Br(),
    html.Div([
    html.H1('Dashの新機能とその他Tips'),
    html.H1('ラズパイはまた今度・・・')],
    style = {'textAlign': 'center' , 'padding': '5% 0 5%', 'margin':'5% 0 5%',  'background': '#EEFFDD'}
    ),
    html.Br(),
    html.H3('合同会社 長目　小川　英幸', style={'textAlign': 'right', 'marginRight': '2%'}),
    html.Div([
    dcc.Link('Go to Next Page', href='/pages/app1')
    ], style = {'textAlign': 'right'}),
], style = {'margin': '5%'})

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')])
def displayPage(pathname):
    if pathname == '/pages/app1':
        return app1.layout 
    elif pathname == '/pages/app2':
        return app2.layout 
    else:
        return indexPage

if __name__ == '__main__':
    app.run_server(debug=True)