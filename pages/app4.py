import dash  
import dash_core_components as dcc 
import dash_html_components as html 
import dash_daq as daq 
import dash_cytoscape as cyto 
from dash_canvas import DashCanvas 
import dash_bio as dashbio 

from dash.dependencies import Input, Output 
from dash.exceptions import PreventUpdate
from dash_canvas.utils import (array_to_data_url, parse_jsonstring,
                              watershed_segmentation)
from skimage import io, color, img_as_ubyte

import numpy as np
import six.moves.urllib.request as urlreq

from app import app 

subTitle = {'textAlign': 'center', 'padding': '1%', 'fontSize': '2vw', 'color': 'blue'}
article = {'fontSize': '1.5vw', 'width': '80%', 'margin': '0 auto 0', 'textAlign': 'left'}
compTitle = {'textAlign': 'Center', 'fontSize': '3vw', 'background': '#EEFFDD', 'marginTop': '5%', 'padding': '1%', 'borderRadius': '20%'}

nodes = [
    {
        'data': {'id': short, 'label': label},
        'position': {'x': 20*lat, 'y': -20*long}
    }
    for short, label, long, lat in (
        ('la', 'Los Angeles', 34.03, -118.25),
        ('nyc', 'New York', 40.71, -74),
        ('to', 'Toronto', 43.65, -79.38),
        ('mtl', 'Montreal', 45.50, -73.57),
        ('van', 'Vancouver', 49.28, -123.12),
        ('chi', 'Chicago', 41.88, -87.63),
        ('bos', 'Boston', 42.36, -71.06),
        ('hou', 'Houston', 29.76, -95.37)
    )
]

edges = [
    {'data': {'source': source, 'target': target}}
    for source, target in (
        ('van', 'la'),
        ('la', 'chi'),
        ('hou', 'chi'),
        ('to', 'mtl'),
        ('mtl', 'bos'),
        ('nyc', 'bos'),
        ('to', 'hou'),
        ('to', 'nyc'),
        ('la', 'nyc'),
        ('nyc', 'bos')
    )
]

elements = nodes + edges

filename = 'https://upload.wikimedia.org/wikipedia/commons/e/e4/Mitochondria%2C_mammalian_lung_-_TEM_%282%29.jpg'
canvas_width = 400 
img = io.imread(filename, as_gray=True)

biodata = urlreq.urlopen("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/alignment_viewer_p53.fasta").read()


layout = html.Div([
    html.Div([
        html.H1('2. Dashの新機能', style={'textAlign': 'center', 'background': '#EEFFDD', 'marginTop': '3%', 'padding': '1%','fontSize': '400%', 'borderRadius':'5%'})
    ]),
    html.Div([
        html.H3('Dash Hands On Returns が1月。それからまた機能が増えています', style={'textAlign': 'center', 'fontSize': '2vw'}),

        html.H3('Dash DAQ', style = subTitle),
        html.P('Dash DAQは実は前から存在していたが、なんかたいしたことないのではと思って見ていなかったが、見てみると凄い。', style = article),
        html.P('DAQとはいろいろな機材を使って行うデータ収集のことで、そのアプリケーションを作るための、きれいな作りのコンポーネントを提供している。スィッチ類も充実しているので、良さげ。簡単に使えるGUIツールって感じです。PythonのGUIツールってあんま簡単な良いものないような。', style = article),
        html.P('今回はこれを使ってラズパイで色々やりたかったが、ラズパイが思いの外難しくて・・・', style = article),

        html.H3('Dash Cytoscape', style = subTitle),
        html.P('ネットワーク構造を作れるコンポーネント。興味深いのだが、データをどのように与えるかが難しいところ。このへんは作成者側でも話されており、Network Xでやればいいやんみたいな話にはなっている。', style = article),
        dcc.Link('Githubでの議論', href='https://github.com/plotly/dash-cytoscape/issues/23', style = {'fontSize':'2vw'}),
        html.P('ネットワーク面白いので本とか読んでいるが、どうやって使うのか、考え中。バイオ系では結構使われているようですね。', style = article),

        html.H3('Dash Canvas', style = subTitle),
        html.P('なんか、絵が描けます。だけだとDAQのように見逃してしまいますが、とんでもなかったです。凄い。', style = article),

        html.H3('Dash Bio', style = subTitle),
        html.P('バイオなグラフが作れます。前までも作れたけど、正直、どうやっているかよく分かりませんでした。', style = article),
        dcc.Link('怖いものもみんなで見れば怖くない！', href='https://github.com/plotly/dash-brain-surface-viewer', style = {'fontSize': '2vw'}),

        html.P('まとめると、DAQはIoTとか工場とかその辺り使えそうなもの。あとの3つはバイオ系でかなり使われるんではないかなぁという感じです。', style=article)
    ], style={'textAlign': 'center', 'margin': '5%', 'padding':'1%' ,'borderRadius': '3%', 'background': '#EEFFDD'}),

    # Dash DAQ
    html.Div([
        html.H3('Dash DAQ', style = compTitle),
        html.Div([
            daq.GraduatedBar(
                id = 'bar1',
                vertical = True,
                color={"gradient":True,"ranges":{"green":[0,8],"yellow":[8,14],"red":[14,20]}},
                size = 500,
                style = {'display': 'inline-block', 'margin': '5%'}
            ),
            daq.GraduatedBar(
                id = 'bar2',
                vertical = True,
                color={"gradient":True,"ranges":{"green":[0,8],"yellow":[8,14],"red":[14,20]}},
                size = 500,
                style = {'display': 'inline-block', 'margin': '5%'}
            ),
            daq.GraduatedBar(
                id = 'bar3',
                vertical = True,
                color={"gradient":True,"ranges":{"green":[0,8],"yellow":[8,14],"red":[14,20]}},
                size = 500,
                style = {'display': 'inline-block', 'margin': '5%'}
            ),
            daq.GraduatedBar(
                id = 'bar4',
                vertical = True,
                color={"gradient":True,"ranges":{"green":[0,8],"yellow":[8,14],"red":[14,20]}},
                size = 500,
                style = {'display': 'inline-block', 'margin': '5%'}
            ),
            daq.GraduatedBar(
                id = 'bar5',
                vertical = True,
                color={"gradient":True,"ranges":{"green":[0,8],"yellow":[8,14],"red":[14,20]}},
                size = 500,
                style = {'display': 'inline-block', 'margin': '5%'}
            ),
            daq.Thermometer(
                id = 'ondoke',
                min = 0,
                max = 100,
                showCurrentValue = True,
                style = {'display': 'inline-block', 'marginLeft': '15%'},
                size = 500
            ),
            dcc.Interval(
                id = 'intervalComp',
                interval = 1000,
                n_intervals = 0
            ),

        ], style = {'marginLeft': '10%'}),

    ], style={'margin': '5%'}),

    html.Div([
        html.Div([
            html.H3(['Dash Cytoscape'], style = compTitle)
                        ]),
                    html.Div([
                        dcc.Dropdown(
                            id='dropdown-update-layout',
                            value='grid',
                            clearable=False,
                            options=[
                            {'label': name.capitalize(), 'value': name}
                            for name in ['grid', 'random', 'circle', 'cose', 'concentric']
                            ], style={'width': '30%', 'margin':'0 auto 0'}
                        ),
                        cyto.Cytoscape(
                            id='cytoscape-update-layout',
                            layout={'name': 'grid'},
                            style={'width': '80%', 'height': '700px', 'margin': '0 auto 0', 'padding': '5%'},
                            elements=elements
                            )
                        ]),
        ], style={'margin': '5%'}),

    # Dash Canvas
    html.Div([
        html.Div([
            html.H3(['Dash Canvas'], style = compTitle)
                        ]),
        html.Div([
            html.H3('絵が描けます'),
            DashCanvas(id = 'canvas1', height= 800),
        ], style={'margin': '3%'}),
        html.Div([
            html.H3('小ネタだけでなく、scikit-imageと組み合わせたら凄いことに！'),
        ]),
        html.Div([
            DashCanvas(id='segmentation-canvas',
               lineWidth=5,
               filename=filename,
               width=canvas_width,
               ),
            ], className="five columns"),
        html.Div([
            html.Img(id='segmentation-img', width=700),
            ], className="five columns"),
    ], style = {'margin': '10%', 'marginBottom': '15%'}),

    # ページ移動
    html.Div([
        dcc.Link('go to next page', href='app5'),
        html.Br(),
        dcc.Link('go back', href='app3'),
        html.Br(),
        dcc.Link('Back to Top', href='/'),
    ], style = {'textAlign': 'right', 'marginRight': '5%'})
])

# DAQ callback

@app.callback([Output('bar1', 'value'),
            Output('bar2', 'value'),
            Output('bar3', 'value'),
            Output('bar4', 'value'),
            Output('bar5', 'value'),
            Output('ondoke', 'value')],
            [Input('IntervalComp', 'n_intervals')])
def passValue(n):
    x1 = np.random.rand()*20
    x2 = np.random.rand()*20
    x3 = np.random.rand()*20
    x4 = np.random.rand()*20
    x5 = np.random.rand()*20
    x6 = x1 + x2 + x3 + x4 + x5
    return x1, x2, x3, x4, x5, x6

# CytoScape callback
@app.callback(dash.dependencies.Output('cytoscape-update-layout', 'layout'),
              [dash.dependencies.Input('dropdown-update-layout', 'value')])
def update_layout(layout):
    return {
        'name': layout,
        'animate': True
    }

@app.callback(Output('segmentation-img', 'src'),
              [Input('segmentation-canvas', 'json_data')])
def segmentation(string):
    if string:
        mask = parse_jsonstring(string, img.shape)
        seg = watershed_segmentation(img, mask)
        src = color.label2rgb(seg, image=img)
    else:
        raise PreventUpdate
    return array_to_data_url(img_as_ubyte(src))

