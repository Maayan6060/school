import dash
from dash import Dash, html

app = Dash(__name__, title="אלתרמן חלל ותעופה", update_title=None)

app.layout = html.Div([
    html.Img(src="/assets/sample.jpg", alt="Sample Image", style={"width": "101%", "height": "73vh", "margin-top": "120px", "margin-left": "-8px"}),
    html.Img(src="/assets/natanya.jpg", alt="Natanya Logo", style={"width": "8%", "height": "12vh", "position": "fixed", 'top': "7%", "left": "45%", "transform": "translate(-50%,-50%)", "z-index": "1000", }),
    html.Img(src="/assets/alterman.jpg", alt="Alterman Logo", style={"width": "20%", "height": "25vh", "position": "fixed", 'top': "7%", "left": "55%", "transform": "translate(-50%,-50%)", "z-index": "1000", })
])
import os

# Get the port number from the environment variable, default to 8050 if not set
port = int(os.getenv('PORT', 8050))

# Run the Dash app on 0.0.0.0 and the port provided by Render
app.run_server(host='0.0.0.0', port=port, debug=True)
