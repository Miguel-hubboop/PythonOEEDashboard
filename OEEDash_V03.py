import dash
from dash import dcc, html
import plotly.graph_objs as go

app = dash.Dash(__name__)

# Dados fictícios para os gráficos
gauge_data = [
    {"label": "OEE", "value": 57, "color": "#7AC943"},
    {"label": "Disponibilidade", "value": 76, "color": "#7AC943"},
    {"label": "Performance", "value": 81, "color": "#7AC943"},
    {"label": "Qualidade", "value": 92, "color": "#7AC943"},
]

gauge_style_height = ""
gauge_style_width = ""

# Layout dos indicadores de performance com gráficos de rosca
gauges = []
for gauge in gauge_data:

    if gauge["label"] == "OEE":
        gauge_style_height = "250px"
        gauge_style_width = "200px"
    else:
        gauge_style_height = "200px"
        gauge_style_width = "150px"
        
    gauges.append(
        html.Div(
            dcc.Graph(
                config={"displayModeBar": False},
                figure=go.Figure(
                    data=[
                        go.Pie(
                            labels=["", gauge["label"]],
                            values=[100-gauge["value"], gauge["value"]],
                            hole=0.6,  # Faz o "donut"
                            marker=dict(colors=["#E1E1E1", gauge["color"]]),
                            textinfo="none",
                        )
                    ],
                    layout=go.Layout(
                        showlegend=False,
                        title=gauge["label"],
                        title_x=0.5,
                        title_y=1,
                        margin=dict(t=0, b=0, l=0, r=0),
                        annotations=[{
                            "text": f'{gauge["value"]}%',
                            "font": {"size": 20},  # Tamanho da fonte do percentual
                            "showarrow": False,
                            "x": 0.5,
                            "y": 0.5,
                        }]
                    )
                ),
                style={"height": gauge_style_height, "width": gauge_style_width}
            ),
            style={"display": "inline-block", "margin": "20px"}
        )
    )

# Layout do dashboard
app.layout = html.Div([
    
    html.Div([
        html.H3("Indicadores de Performance", style={"textAlign": "left", "margin-bottom": "20px"}),
        html.Div(gauges, style={"display": "flex", "justify-content": "space-around", "margin-bottom": "40px", "flex-wrap": "nowrap"}),
    ], style={"padding": "10px", "backgroundColor": "#ffffff", "borderRadius": "5px", "width": "70%", "display": "inline-block"}),


    html.Div([
        html.H3("Status da Máquina", style={"textAlign": "left", "margin-bottom": "20px", "color": "white"}),
        html.Div([
            html.H4("Turno", style={"textAlign": "left", "color": "black", "position": "relative", "top": "-15px"}),
            html.H2("Primeiro", style={"textAlign": "center", "color": "black", "position": "relative", "top": "-40px"}),
        ], style={"backgroundColor": "#FFFFFF","padding": "5px", "height": "60px", "width": "300px", "position": "relative", "left": "10px", "borderRadius": "5px"}),
        html.Div([
            html.H4("Operação", style={"textAlign": "left", "color": "black", "position": "relative", "top": "-15px"}),
            html.H2("Parada", style={"textAlign": "center", "color": "black", "position": "relative", "top": "-40px"}),
        ], style={"backgroundColor": "#FFFFFF","padding": "5px", "height": "60px", "width": "300px", "position": "relative", "left": "10px", "top": "20px", "borderRadius": "5px"}),
        html.Div([
            html.H4("Consumo diário", style={"textAlign": "left", "color": "black", "position": "relative", "top": "-15px"}),
            html.H3("R$00,00", style={"textAlign": "center", "color": "black", "position": "relative", "top": "-20px"}),
            html.H3("000 kWh", style={"textAlign": "center", "color": "black", "position": "relative", "top": "-35px"}),
        ], style={"backgroundColor": "#FFFFFF","padding": "5px", "height": "100px", "width": "300px", "position": "relative", "left": "10px", "top": "50px", "borderRadius": "5px"}),
    ], style={"backgroundColor": "#FF585D", "borderRadius": "5px", "padding": "5px", "height": "400px", "width": "26%", "display": "inline-block", "verticalAlign": "top", "margin-left": "0px"}),


    html.Div([
        html.H3("Progressão dos tempos", style={"textAlign": "left", "margin-bottom": "10px"}),
        html.Div([
            html.Div([
                html.H4("Turno 1"),
                html.Div([
                    html.Div(style={"width": "60%", "height": "30px",  "backgroundColor": "#7AC943", "display": "inline-block"}),
                    html.Div(style={"width": "10%", "height": "30px",  "backgroundColor": "#FF585D", "display": "inline-block"}),
                    html.Div(style={"width": "10%", "height": "30px",  "backgroundColor": "#F7941D", "display": "inline-block"}),
                    html.Div(style={"width": "20%", "height": "30px",  "backgroundColor": "#7AC943", "display": "inline-block"}),
                ], style={"textAlign": "left", "width": "390px"})
            ], style={"padding": "5px", "display": "inline-block"}),

            html.Div([
                html.H4("Turno 2"),
                html.Div([
                    html.Div(style={"width": "70%", "height": "30px", "backgroundColor": "#7AC943", "display": "inline-block"}),
                    html.Div(style={"width": "20%", "height": "30px", "backgroundColor": "#FF585D", "display": "inline-block"}),
                    html.Div(style={"width": "10%", "height": "30px", "backgroundColor": "#F7941D", "display": "inline-block"}),
                ], style={"textAlign": "left", "width": "390px"})
            ], style={"padding": "5px", "display": "inline-block"}),

            html.Div([
                html.H4("Turno 3"),
                html.Div([
                    html.Div(style={"width": "90%", "height": "30px", "backgroundColor": "#7AC943", "display": "inline-block"}),
                    html.Div(style={"width": "5%", "height": "30px", "backgroundColor": "#FF585D", "display": "inline-block"}),
                    html.Div(style={"width": "5%", "height": "30px", "backgroundColor": "#F7941D", "display": "inline-block"}),
                ], style={"textAlign": "left", "width": "390px"})
            ], style={"padding": "5px", "display": "inline-block"}),

        ], style={"backgroundColor": "#f4f4f4", "padding": "10px", "borderRadius": "5px", "display": "inline-block", "width": "96%"}),
    ], style={"margin-top": "10px"}),

], style={"font-family": "Arial", "backgroundColor": "#E2E2E2", "padding": "30px", "borderRadius": "10px"})

if __name__ == '__main__':
    app.run_server(debug=True)
