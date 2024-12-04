import dash
from dash import Dash, html, Input, Output
import os

app = Dash(__name__, title="אלתרמן חלל ותעופה", update_title=None)

app.layout = html.Div([
    #school image:
    html.Img(src="/assets/sample.jpg", alt="Sample Image", style={"width": "101%", "height": "90vh", "margin-top": "-10px", "margin-left": "-8px"}),
    #netanya logo image:
    html.Img(src="/assets/natanya.jpg", alt="Natanya Logo", style={"width": "4%", "height": "8vh", "position": "fixed", 'top': "5%", "left": "3%", "transform": "translate(-50%,-50%)", "z-index": "1000", }),
    #school logo image:
    html.Img(src="/assets/alterman.jpg", alt="Alterman Logo", style={"width": "11%", "height": "16vh", "position": "fixed", 'top': "4%", "left": "8%", "transform": "translate(-50%,-50%)", "z-index": "1000", }),
    #white (transperent) horizontal line:
    html.Div(style={'position': 'absolute', 'top': '20%', 'left': '0%', 'width': '100%', 'borderTop': '100px solid white', 'opacity': '0.7'}),
    #School name text:
    html.Div(children='חטיבת ביניים חלל ותעופה ע"ש אלתרמן',style={'position': 'absolute', 'top': '19%', 'left': '5%', 'fontSize': '100px', 'color': '#003151', 'fontFamily': 'BN Alpaca' }),
    #Menu line:
    html.Div(style={'position': 'fixed', 'top': '0%', 'left': '0%', 'width': '100%', 'borderTop': '100px solid #883000', 'opacity': '0.8'}),
    #Button 1 - test schedules:
    html.Button("לוח מבחנים", id='test', style={'position': 'fixed', 'backgroundColor': 'blue', 'color': 'white', 'padding': '10px 20px', 'border': 'none', 'borderRadius': '5px', 'cursor': 'pointer', 'fontSize': '20px', 'top': '3%', 'left': '30%'})
])

port = int(os.getenv('PORT', 8050))
app.run_server(host='0.0.0.0', port=port, debug=True)
