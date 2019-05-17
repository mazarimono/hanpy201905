import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go 
import numpy as np 

from app import app
import pandas as pd 
from datetime import datetime 
from datetime import timedelta 

df = pd.read_csv('./data/longform2.csv', index_col=0)

dfkyoto = pd.read_csv('./data/kyoto_hotel_comp1.csv', index_col=0)
mapbox_access_token = "pk.eyJ1IjoibWF6YXJpbW9ubyIsImEiOiJjanA5Y3IxaWsxeGtmM3dweDh5bjgydGFxIn0.3vrfsqZ_kGPGhi4_npruGg"

dfjpy = pd.read_csv('https://raw.githubusercontent.com/plotly/dash-web-trader/master/pairs/USDJPY.csv', index_col=1, parse_dates=['Date'])
dffjpy = dfjpy['2016/1/5']
dffjpy = dffjpy.resample('1S').last().bfill()

layout = html.Div([
    html.Div([
        html.H1('1. Dashとは？', style={'textAlign': 'center', 'background': '#EEFFDD', 'marginTop': '3%', 'padding': '1%','fontSize': '400%', 'borderRadius':'5%'})
    ]),
    html.Div([
        dcc.Markdown('''
            DashとはFlask, Plotly.js, React.jsで作られたウェブフレームワークです。

            Plotly.jsが可視化ライブラリのため、可視化が簡単にウェブで共有できます。

            そして、その可視化をインタラクティブに動かせるというのも特徴です。

            このためかなり多くのデータを、細かく見られます。

        ''')
    ], style={'fontSize': '250%', 'textAlign': 'center', 'margin': '5%', 'padding':'1%' ,'borderRadius': '3%', 'background': '#EEFFDD'}),

    html.Div([
         html.Div([
                    html.H3('都道府県別人口とGDP,一人当たりGDP', style={
                        'textAlign': 'center', 'fontSize':'300%', 'background': '#EEFFDD'
                        }),
                    html.Div([
                    html.Div([
                        dcc.Graph(id = 'scatter-chart',
                        hoverData = {'points': [{'customdata': '大阪府'}]},
                        ),
                    dcc.Slider(
                        id = 'slider-one',
                        min = df['year'].min(),
                        max = df['year'].max(),
                        marks = {i: '{}'.format(i) for i in range(int(df['year'].min()), int(df['year'].max())) if i % 2 == 1},
                        value = 1955,
                        )
                        ], style={
                            'display': 'inline-block',
                            'width': '60%',
                            }),
                    html.Div([
                        dcc.Graph(id='chart-one'),
                        dcc.Graph(id='chart-two'),
                        dcc.Graph(id='chart-three'),
                    ],style={
                        'display': 'inline-block',
                        'width': '39%'
                        })
                    ], style={'background': '#EEFFDD', 'padding':'1%'}),
                    ])
    ]),
    html.Div([
        html.Div([
            html.H3(['ライブアップデートも！'], style = {'textAlign': 'Center', 'fontSize': '300%', 'background': '#EEFFDD', 'marginTop': '5%'})
                ]),
        html.Div([
            dcc.Graph(id="usdjpy"),
            dcc.Interval(
                id = 'interval_components',
                interval = 1000,
                        )
                ], style={'height': '30%', 'width': '80%', 'margin': '0 auto 0', 'textAlign': 'center','background': '#EEFFDD'}),
    ]),
    html.Div([
        html.Div([
                    html.H3(['マップも表示可能です！'], style = {'textAlign': 'Center', 'fontSize': '250%', 'background': '#EEFFDD', 'marginTop': '5%'})
                ]),
                dcc.Graph(
                    id = 'kyoto-hotels',
                    figure = {
                        'data':[
                        go.Scattermapbox(
                        lat = dfkyoto[dfkyoto['age']== i]['ido'],
                        lon = dfkyoto[dfkyoto['age']== i]['keido'],
                        mode = 'markers',
                        marker = dict(
                        size=9
                        ),
                        text = dfkyoto[dfkyoto['age']== i]['hotel_name'],
                        name = str(i),
                        ) for i in dfkyoto['age'].unique()
                        ],
                        'layout':
                        go.Layout(
                            autosize=True,
                            hovermode='closest',
                            mapbox = dict(
                            accesstoken=mapbox_access_token,
                            bearing = 0,
                            center = dict(
                            lat=np.mean(dfkyoto['ido']),
                            lon=np.mean(dfkyoto['keido'])
                        ),
                        pitch = 90,
                        zoom=10,
                    ),
                    height=800
                        )
                    }
                    )
    ], style={'padding':50}),
    html.Div([
        dcc.Link('go to next page', href='app4'),
        html.Br(),
        dcc.Link('go back', href='app2'),
        html.Br(),
        dcc.Link('Back to Top', href='/'),
    ], style = {'textAlign': 'right', 'marginRight': '5%'})
])

@app.callback(
    Output('scatter-chart', 'figure'),
    [Input('slider-one', 'value')]
)
def update_graph(selected_year):
    dff = df[df['year'] == selected_year]
    dffper = dff[dff['item']=='pergdp']
    dffgdp = dff[dff['item']== 'GDP']
    dffpop = dff[dff['item']== 'popu']

    return {
        'data': [go.Scatter(
            x = dffper[dffper['area']==i]['value'],
            y = dffgdp[dffgdp['area']==i]['value'],
            mode = 'markers',
            customdata = [i],
            marker={
                'size' : dffpop[dffpop['area']==i]['value']/100,
                'color': dffpop[dffpop['area']==i]['color'],
            }, 
            name=i,
        )for i in dff.area.unique()],
        'layout': {
            'height': 800,
            'title': '{}年の都道府県GDP、一人当たりGDP、人口（円の大きさ）'.format(selected_year),
            'paper_bgcolor': '#EEFFDD',
            'fontSize': "2rem",
            'xaxis': {
                'type': 'log',
                'title': '都道府県別一人当たりGDP(log scale)',
                'range':[np.log(80), np.log(1200)]
            },
            'yaxis': {
                'type':'log',
                'title': '都道府県別GDP(log scale)',
                'range':[np.log(80), np.log(8000)]
            },
            'hovermode': 'closest',
        }
    }

def create_smallChart(dff, area, name):
    return {
        'data':[go.Scatter(
            x = dff['year'],
            y = dff['value']
        )],
        'layout':{
            'height': 300,
            'title': '{}の{}データ'.format(area, name),
            'paper_bgcolor': '#EEFFDD',
        }
    }



@app.callback(
    Output('chart-one', 'figure'),
    [(Input('scatter-chart', 'hoverData'))]
)
def createGDP(hoverdata):
    areaName = hoverdata['points'][0]['customdata']
    dff = df[df['area']==areaName]
    dff = dff[dff['item'] == 'GDP']
    return create_smallChart(dff, areaName, 'GDP')

@app.callback(
    Output('chart-two', 'figure'),
    [(Input('scatter-chart', 'hoverData'))]
)
def createPerGDP(hoverdata):
    areaName = hoverdata['points'][0]['customdata']
    dff = df[df['area']==areaName]
    dff = dff[dff['item'] == 'pergdp']
    return create_smallChart(dff, areaName, 'pergdp')

@app.callback(
    Output('chart-three', 'figure'),
    [(Input('scatter-chart', 'hoverData'))]
)
def createPopu(hoverdata):
    areaName = hoverdata['points'][0]['customdata']
    dff = df[df['area']==areaName]
    dff = dff[dff['item'] == 'popu']
    return create_smallChart(dff, areaName, 'popu')

@app.callback(
    Output('usdjpy', 'figure'),
    [Input('interval_components', 'n_intervals')]
)
def update_graph(n):
    t = datetime.now()
    nowHour = t.hour
    nowMinute = t.minute 
    nowSecond = t.second 

    d = datetime(2016, 1, 5, nowHour, nowMinute, nowSecond)
    period = timedelta(seconds = 180)
    d1 = d - period 
    dffjpy1 = dffjpy.loc['{}'.format(d1): '{}'.format(d), :]

    return {
        'data': [go.Scatter(
            x = dffjpy1.index,
            y = dffjpy1['Bid']
        )],
        'layout':{
            'height': 600,
            'title': 'USD-JPY 1Second Charts'
        }
    }