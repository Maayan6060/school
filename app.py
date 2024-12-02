import dash
from dash import Dash, html
import os

app = Dash(__name__, title="אלתרמן חלל ותעופה", update_title=None)

app.layout = html.Div([
    #school image:
    html.Img(src="/assets/sample.jpg", alt="Sample Image", style={"width": "101%", "height": "90vh", "margin-top": "-10px", "margin-left": "-8px"}),
    #netanya logo image:
    html.Img(src="/assets/natanya.jpg", alt="Natanya Logo", style={"width": "4%", "height": "8vh", "position": "fixed", 'top': "5%", "left": "3%", "transform": "translate(-50%,-50%)", "z-index": "1000", }),
    #school logo image:
    html.Img(src="/assets/alterman.jpg", alt="Alterman Logo", style={"width": "11%", "height": "16vh", "position": "fixed", 'top': "4%", "left": "8%", "transform": "translate(-50%,-50%)", "z-index": "1000", }),
    #white (transperent) logo line:
    html.Div(style={'position': 'absolute', 'top': '20%', 'left': '0%', 'width': '100%', 'borderTop': '100px solid white', 'opacity': '0.7'}),
    #School name text:
    html.Div(children='חטיבת ביניים חלל ותעופה ע"ש אלתרמן',style={'position': 'fixed', 'top': '19%', 'left': '5%', 'fontSize': '100px', 'color': '#003151', 'fontFamily': 'BN Alpaca' })

])

port = int(os.getenv('PORT', 8050))
app.run_server(host='0.0.0.0', port=port, debug=True)
