# dash_simulation_app.py
# Simplified educational model - no patient data used
# Author: Dr. Eldirdiri Fadol, Dr. Moumena Aboulsalam
# Affiliation: European Nile University & ATLANTA for Liberty Studies
# License: CC-BY 4.0

import numpy as np
import plotly.graph_objs as go
from dash import Dash, html, dcc, Input, Output

# Initialize Dash app
app = Dash(__name__)
server = app.server

# Layout
app.layout = html.Div([
    html.H2("Interactive Simulation: Posterior Aortic Displacement"),
    html.P("Synthetic visualization of hemodynamic changes at the clavicular level"),
    
    dcc.Slider(
        id='displacement',
        min=0, max=50, step=1, value=20,
        marks={0: 'Normal', 25: 'Moderate', 50: 'Severe'}
    ),
    html.Div(id='disp-value', style={'margin': '10px 0'}),
    dcc.Graph(id='hemodynamic-plot')
])

# Callback to update visualization
@app.callback(
    [Output('hemodynamic-plot', 'figure'),
     Output('disp-value', 'children')],
    Input('displacement', 'value')
)
def update_plot(disp):
    # Synthetic data (no patient info)
    x = np.linspace(0, 2*np.pi, 100)
    baseline = np.sin(x)
    altered = np.sin(x - disp/100) * (1 - disp/150)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=baseline, mode='lines', name='Normal Flow', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=x, y=altered, mode='lines', name='Posteriorly Displaced Flow', line=dict(color='red')))
    fig.update_layout(
        title="Relative Flow Profiles",
        xaxis_title="Normalized Vessel Distance",
        yaxis_title="Relative Flow Intensity",
        template="plotly_white",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    msg = f"Posterior displacement intensity: {disp}%"
    return fig, msg

# Run app
if __name__ == "__main__":
    app.run_server(debug=True)
