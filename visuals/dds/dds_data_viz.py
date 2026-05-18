import threading
import webbrowser
from dash import Dash, dcc, html
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import time

# -----------------------------
# 1. MATURITY RADAR
# -----------------------------
def run_radar():
    app = Dash(__name__)

    categories = ['Data Quality', 'Integration', 'Skills', 'Governance', 'Technology', 'Culture']

    current = [2, 1, 3, 2, 3, 2]
    target = [5, 4, 4, 5, 4, 5]

    fig = go.Figure()


    fig.add_trace(go.Scatterpolar(
        r=target,
        theta=categories,
        fill='toself',
        name='Target State'
    ))

    fig.add_trace(go.Scatterpolar(
        r=current,
        theta=categories,
        fill='toself',
        name='Current State'
    ))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
        title="Digital & Data Maturity: Current vs Target minimum (2030)"
    )

    app.layout = html.Div([
        html.H2("Maturity Shift"),
        dcc.Graph(figure=fig)
    ])

    def open_browser():
        time.sleep(1)
        webbrowser.open("http://127.0.0.1:8050")

    threading.Thread(target=open_browser).start()
    app.run(port=8050)


# -----------------------------
# 2. ROADMAP TIMELINE
# -----------------------------
def run_roadmap():
    app = Dash(__name__)

    df = pd.DataFrame([
        dict(Task="Data Catalogue MVP", Start="2026-01-01", Finish="2026-06-01", Theme="Data"),
        dict(Task="Corporate Lakehouse & Data Engineering", Start="2026-03-01", Finish="2027-03-01", Theme="Technology"),
        dict(Task="Consolidated Data Platform", Start="2026-10-01", Finish="2027-10-01", Theme="Technology"),
        dict(Task="Data Lab Launch", Start="2026-06-01", Finish="2027-01-01", Theme="Innovation"),
        dict(Task="AI Adoption & Ethics", Start="2027-01-01", Finish="2028-01-01", Theme="Innovation"),
        dict(Task="Data Skills & Literacy", Start="2026-01-01", Finish="2028-12-31", Theme="People"),
        dict(Task="Data Governance Framework", Start="2026-01-01", Finish="2026-12-31", Theme="Governance"),
    ])

    fig = px.timeline(
        df,
        x_start="Start",
        x_end="Finish",
        y="Task",
        color="Theme"
    )

    fig.update_layout(
        title="Digital & Data Strategy Roadmap",
        xaxis_title="Timeline",
        yaxis_title=""
    )

    app.layout = html.Div([
        html.H2("Strategy Roadmap"),
        dcc.Graph(figure=fig)
    ])

    def open_browser():
        time.sleep(1)
        webbrowser.open("http://127.0.0.1:8051")

    threading.Thread(target=open_browser).start()
    app.run(port=8051)


# -----------------------------
# 3. SYSTEM TRANSFORMATION
# -----------------------------
def run_transformation():
    app = Dash(__name__)

    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            label=[
                "Legacy Systems", "Spreadsheets", "Siloed Data", "Dispersed Data Teams"
                "Data Lakehouse", "Integrated Platform", "Decision Making",
                "Centralised Digital & Data, LOB data excellence"
            ]
        ),
        link=dict(
            source=[0, 1, 2],
            target=[3, 3, 4],
            value=[5, 4, 6]
        )
    )])

    fig.update_layout(title_text="From Fragmented Systems & Structure to Integrated Data Platform & Services")

    app.layout = html.Div([
        html.H2("System Transformation"),
        dcc.Graph(figure=fig)
    ])

    def open_browser():
        time.sleep(1)
        webbrowser.open("http://127.0.0.1:8052")

    threading.Thread(target=open_browser).start()
    app.run(port=8052)


# -----------------------------
# RUN ALL THREE
# -----------------------------
if __name__ == '__main__':
    threading.Thread(target=run_radar).start()
    threading.Thread(target=run_roadmap).start()
    threading.Thread(target=run_transformation).start()
