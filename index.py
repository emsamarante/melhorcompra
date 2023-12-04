import dash
import dash_bootstrap_components as dbc
from dash import html, dcc 
from dash.dependencies import Output, Input, State
from app import *


style_card = {
            'min-height': '400px',
            'width':'100%',
            'padding-left':'25px',
            'padding-top':'25px',
            'padding-right':'25px',
            'align-self':'center'
            }

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Legend("Compare os preços!"),
                html.P("Use . 'ponto' no lugar da , 'vírgula'"),
                html.Br(), 
                dbc.Row([
                    dbc.Col([
                        dbc.Row([html.Label("Digite o preço do produto A: "),]),
                        dbc.Row([dcc.Input(id="preco_prod_A", placeholder="ex: 35.97", type='number')]),
                ], sm=5, lg=5),
                    dbc.Col([],sm=1, lg=1),
                    dbc.Col([
                        dbc.Row([html.Label("Digite a quantidade do produto A: "),]),
                        dbc.Row([dcc.Input(id="qtd_prod_A", placeholder="apenas os números", type='number')]),
                        html.Br()
                ], sm=5, lg=5)
            ]),
                dbc.Row([
                    dbc.Col([
                        dbc.Row([html.Label("Digite o preço do produto B: "),]),
                        dbc.Row([dcc.Input(id="preco_prod_B", placeholder="ex: 35.97", type='number')])    
                ], sm=5, lg=5),
                    dbc.Col([],sm=1, lg=1),
                    dbc.Col([
                        dbc.Row([html.Label("Digite a quantidade do produto B: "),]),
                        dbc.Row([dcc.Input(id="qtd_prod_B", placeholder="apenas os números", type='number')])
                ], sm=5, lg=5)
            ], style={'margin-top':'2%'}),
                dbc.Row([
                    html.Div(children = [
                        html.Br(),
                        html.H3(id="resultado")])
                ])
            ], style=style_card)
        ], style={'height': '100vh', 'display':'flex', 'justify-content':'center'})
    ])
], fluid=True)

@app.callback(
    Output("resultado", "children"),
    [Input("preco_prod_A", "value"),
     Input("qtd_prod_A", "value"),
     Input("preco_prod_B", "value"),
     Input("qtd_prod_B", "value")
    ]
)

def calcula(precoA, qtdA, precoB, qtdB):
    
    # print("Aqui")
    if precoA and precoB and qtdA and qtdB:
        precoA = float(precoA)
        precoB = float(precoB)
        qtdA = float(qtdA)
        qtdB = float(qtdB)
        
        if (precoA/qtdA) > (precoB/qtdB):
            return f"O produto A está mais caro que o produto B."
        elif (precoA/qtdA) < (precoB/qtdB):
            return f"O produto A está mais barato que o produto B."  
        else:
            return f"Tanto faz comprar o produto A quanto o B."
    else:
        return "Preencha todos os campos!"
    
if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0')