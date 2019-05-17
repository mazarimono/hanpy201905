import dash  
import dash_bio as dashbio 
import dash_core_components as dcc 
import dash_html_components as html
import dash_daq as daq 
import six.moves.urllib.request as urlreq
import json
from numpy import random 

from app import app 

data = urlreq.urlopen("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/alignment_viewer_p53.fasta").read().decode('utf-8')

model_data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/mol3d/model_data.js').read()
styles_data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/mol3d/styles_data.js').read()
model_data = json.loads(model_data)
styles_data = json.loads(styles_data)


compTitle = {'textAlign': 'Center', 'fontSize': '3vw', 'background': '#EEFFDD', 'marginTop': '5%', 'padding': '1%', 'borderRadius': '20%'}

layout = html.Div([
    html.H3('Dash Bio', style=compTitle),
    html.H3('アライメントチャートと呼ばれるチャート', style = {'textAlign': 'center', 'margin': '3%'}),
    dashbio.AlignmentChart(
        id='my-alignment-viewer',
        data=data
    ),
    html.Div(id='alignment-viewer-output'),
    html.Div([
        html.H3('やったった感が得られる３Dチャート4行！', style = {'textAlign': 'center', 'margin': '3%'}),
        dashbio.Molecule3dViewer(
            styles=styles_data,
            modelData=model_data,
            selectionType='Chain'
            )
    ], style={'margin': '10%'}),

    # TIPS1
    html.Div([
        html.H3('TIPS　1', style = compTitle),
        html.Div([
            html.H3('Dashに再生ボタンない問題', style = {'textAlign': 'center', 'margin': '3%'}),
            html.Div([
                daq.LEDDisplay(
                    id = 'leddisplay',
                    value = 0.00000,
                    size = 100,
                    color = 'green',
                    backgroundColor = 'skyblue',
                    style = {'margin': '5%'}
                ),
                daq.ToggleSwitch(
                    id = 'switch',
                    value = True,
                    size = 100,
                    color = 'green',
                    style={'margin': '5%'}
                ),
                dcc.Interval(
                    id = 'intervals',
                    interval = 1000,
                    n_intervals = 0,
                ),
            ]),
        html.H3('ツールを使えばできるよ！',style = {'margin': '5%', 'textAlign': 'center'}),
        html.H3('ここではインターバルとDAGのボタンとコールバックを使って再生ボタンを動かしました。',style = {'margin': '5%', 'textAlign': 'center'})
        ]),
    ],style ={'margin': '5%'}),

    # TIPS2
    html.Div([
        html.H3('TIPS 2', style = compTitle),
        html.H3('これまでは一つのファイルに書いていたが、結果・・・',style = {'margin': '5%', 'textAlign': 'center'}),
        html.Div([
        dcc.Link('2000行ほどあり、下にコールバックのあるとんでもない・・姿に・・', href = 'https://github.com/mazarimono/pydataosaka/blob/master/app.py')], style = {'margin': '0 auto 0', 'width': '50%', 'fontSize': '2vw'}),
        html.H3('もうこれではだめだ・・ということで・・',style = {'margin': '5%', 'textAlign': 'center', 'textAlign': 'center'}),
        html.Div([
        dcc.Link('ファイルを分けることに。', href = 'https://dash.plot.ly/urls')], style = {'margin': '0 auto 0', 'width': '50%', 'fontSize': '2vw', 'textAlign': 'center'}),
        html.H3('なんか色々分け方がありましたが、今回はページごとにファイルを分けました。', style = {'margin': '5%', 'textAlign': 'center'}),
        html.Div([
        dcc.Link('こんな感じに', href = 'https://github.com/mazarimono/hanpy201905')], style = {'margin': '0 auto 0', 'width': '50%', 'fontSize': '2vw', 'textAlign': 'center'}),
        html.H3('しかし分けたおかげで、herokuへのあげ方が分かりませんでした。', style = {'margin': '5%', 'textAlign': 'center'} )
    ]),

    # まとめ
    html.Div([
        html.H3('まとめ', style = compTitle),
        html.H3('こんな感じでとんでもない勢いで新たなツールが出てきています。', style = {'margin': '5%', 'textAlign': 'center'}),
        html.H3('しかも可視化が必要そうなところにガンガン注力しているので、今後もチェックしていきたいと思います。', style = {'margin': '5%', 'textAlign': 'center'}),
    ]),

    # ページ移動
    html.Div([
        dcc.Link('go back', href='app4'),
        html.Br(),
        dcc.Link('Back to Top', href='/'),
    ], style = {'textAlign': 'right', 'marginRight': '5%'})
])

@app.callback(
    dash.dependencies.Output('alignment-viewer-output', 'children'),
    [dash.dependencies.Input('my-alignment-viewer', 'eventDatum')]
)
def update_output(value):
    if value is None:
        return 'No data.'
    return str(value)

@app.callback(
    dash.dependencies.Output('intervals', 'disabled'),
    [dash.dependencies.Input('switch', 'value')])
def wakeUp(value):
    return value

@app.callback(dash.dependencies.Output('leddisplay', 'value'),
            [dash.dependencies.Input('intervals', 'n_intervals')])
def bearNum(n):
    x = random.rand()
    return x

