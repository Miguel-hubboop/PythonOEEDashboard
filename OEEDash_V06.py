import streamlit as st
import plotly.graph_objs as go
import requests

response = requests.get('https://yj8ityf.localto.net/plc-data')
plc_data = response.json()['plc_data']
st.write(plc_data)

# Dados fictícios para os gráficos
gauge_data = [
    {"label": "OEE", "value": plc_data, "color": "#7AC943"},
    {"label": "Disponibilidade", "value": 76, "color": "#7AC943"},
    {"label": "Performance", "value": 81, "color": "#7AC943"},
    {"label": "Qualidade", "value": 92, "color": "#7AC943"},
]

# Layout dos indicadores de performance com gráficos de rosca
def create_gauge(gauge):
    # Definir o tamanho do gráfico baseado no rótulo
    if gauge["label"] == "OEE":
        gauge_style_height = "250px"
        gauge_style_width = "200px"
    else:
        gauge_style_height = "200px"
        gauge_style_width = "150px"

    # Gráfico de rosca
    fig = go.Figure(
        data=[
            go.Pie(
                labels=["", gauge["label"]],
                values=[100 - gauge["value"], gauge["value"]],
                hole=0.6,
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
                "font": {"size": 20},
                "showarrow": False,
                "x": 0.5,
                "y": 0.5,
            }]
        )
    )

    return fig

# Título do Dashboard
st.title("Indicadores de Performance")

# Organizar os gráficos em colunas para manter o layout
cols = st.columns(4)
for i, gauge in enumerate(gauge_data):
    with cols[i]:
        st.plotly_chart(create_gauge(gauge), use_container_width=True)

# Seção "Status da Máquina"
st.header("Status da Máquina")

status_cols = st.columns(3)

with status_cols[0]:
    st.subheader("Turno")
    st.text("Primeiro")
with status_cols[1]:
    st.subheader("Operação")
    st.text("Parada")
with status_cols[2]:
    st.subheader("Consumo diário")
    st.text("R$00,00")
    st.text("000 kWh")

# Seção "Progressão dos tempos"
st.header("Progressão dos tempos")

turnos = [
    {"label": "Turno 1", "data": [60, 10, 10, 20]},
    {"label": "Turno 2", "data": [70, 20, 10]},
    {"label": "Turno 3", "data": [90, 5, 5]},
]

for turno in turnos:
    st.subheader(turno["label"])
    st.progress(sum(turno["data"]))
