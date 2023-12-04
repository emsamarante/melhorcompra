import dash
import dash_bootstrap_components as dbc


tema = dbc.themes.QUARTZ
FONT_AWESOME = ["https://use.fontawesome.com/releases/v5.15.4/css/all.css"]
BS = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css"



app = dash.Dash(__name__, external_stylesheets=[tema])
server = app.server
#app.config.suppress_callback_exceptions = True


