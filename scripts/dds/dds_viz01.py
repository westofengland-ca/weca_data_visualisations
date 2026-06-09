import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

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

# Save as a standalone .html file within the visuals folder
fig.write_html(r"visuals/dds/viz01/index.html", include_plotlyjs="cdn")