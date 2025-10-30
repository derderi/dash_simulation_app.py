import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np

# Initialize the app
app = dash.Dash(__name__)
app.title = "Thoracic Vessel Displacement Simulation"

# Layout
app.layout = html.Div(
    style={"fontFamily": "Arial", "padding": "20px"},
    children=[
        html.H2("Simulation of Posterior Aortic Displacement at the Clavicular Level"),
        html.P(
            "This interactive model demonstrates how posterior displacement of the aortic arch "
            "affects vessel geometry and potential compression zones. Use the slider to adjust "
            "the displacement level and observe changes in hemodynamic profiles."
        ),
        dcc.Slider(
            id="displacement-slider",
            min=0,
            max=100,
            step=5,
            value=30,
            marks={i: f"{i}%" for i in range(0, 101, 20)},
        ),
        dcc.Graph(id="vessel-graph"),
        html.P(
            "© 2025 Eldirdiri Fadol & Moumena Aboulsalam — "
            "European Nile University & ATLANTA for Liberty Studies",
            style={"fontSize": "13px", "marginTop": "20px", "color": "#666"},
        ),
    ],
)

# Callback: Update plot when slider moves
@app.callback(
    Output("vessel-graph", "figure"),
    Input("displacement-slider", "value"),
)
def update_graph(displacement):
    x = np.linspace(0, 10, 200)
    normal_aorta = np.sin(x)
    displaced_aorta = np.sin(x + displacement / 50.0)
    vein = np.sin(x - 0.5)

    fig = go.Figure()

    # Normal vessels
    fig.add_trace(go.Scatter(x=x, y=normal_aorta, mode="lines", name="Normal Aorta", line=dict(color="red", width=3)))
    fig.add_trace(go.Scatter(x=x, y=vein, mode="lines", name="Vein (SVC)", line=dict(color="blue", width=3)))

    # Displaced vessel
    fig.add_trace(
        go.Scatter(
            x=x, y=displaced_aorta, mode="lines", name="Posteriorly Displaced Aorta",
            line=dict(color="darkred", width=3, dash="dash")
        )
    )

    fig.update_layout(
        title=f"Posterior Displacement Simulation ({displacement}% shift)",
        xaxis_title="Relative Thoracic Position",
        yaxis_title="Flow Path Amplitude",
        template="simple_white",
        legend=dict(x=0.02, y=1.08, orientation="h"),
        margin=dict(l=40, r=40, t=70, b=40)
    )

    return fig


# Run the app (Dash 3+)
if __name__ == "__main__":
    app.run(debug=True)
