import dash  
import dash_core_components as dcc 
import dash_html_components as html 
import dash_daq as daq 
import dash_cytoscape as cyto 
import dash_canvas 

from app import app 


layout = html.Div([
    html.Div([
        html.H1('2. Dashの新機能', style={'textAlign': 'center', 'background': '#EEFFDD', 'marginTop': '3%', 'padding': '1%','fontSize': '400%', 'borderRadius':'5%'})
    ]),
    html.Div([
        dcc.Markdown('''
            Dash Hands On Returnsが1月。それから多くの機能が追加されました。

            dash DAQ / データの獲得とエンジニアアプリケーションをきれいに作るコンポーネント

                        DAQというのはどうもデータ収集のことらしく、
                    
                        工場系の機械なんかとつないだサンプルがある。

                    https://www.dashdaq.io/  カッコの良いサイトが作られている。

                    前からあったけど、存在感なかった。注目してみると色々使えそう。

            dash Cytoscape /  ネットワーク構造を作る。面白い。グラフ系の本をたまたま読んでいたので、

                    活用方法を考え中。データをどうやって食わすか問題があって、Network X というので

                    やりましょか？みたいな話になっているようだ。この辺りデータがあっても
                    
                    どうやって、これに入れたらよいか、難しいところもある。

            dash canvas  /   絵が描けます。なんだそれと思っていたら、とんでもないことができた。

                    めちゃ強い。

            dash Bio  /   バイオな画像を作る。しかし、Windowsでpip install 出来ず・・・・

        ''')
    ], style={'fontSize': '250%', 'textAlign': 'center', 'margin': '5%', 'padding':'1%' ,'borderRadius': '3%', 'background': '#EEFFDD'}),
])