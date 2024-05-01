import pandas as pd
import plotly.graph_objs as go

# Read the CSV file
df = pd.read_csv(r"C:\Users\arpit\My_PC\repos\SwiftML\misc\test.csv")

# Extracting models and metrics data
models = df.index.tolist()
metrics = df.columns.tolist()

# Line Plot for Metrics Over Different Models
fig1 = go.Figure()
for metric in metrics:
    fig1.add_trace(go.Scatter(x=models, y=df[metric], mode='lines+markers', name=metric))
fig1.update_layout(title='Metrics Over Different Models', xaxis_title='Model', yaxis_title='Metric Value')

# Scatter Plot for R2 vs. Other Metrics
fig2 = go.Figure()
for metric in metrics[:-1]:
    fig2.add_trace(go.Scatter(x=df['R2'], y=df[metric], mode='markers', name=metric))
fig2.update_layout(title='R2 vs. Other Metrics', xaxis_title='R2', yaxis_title='Metric Value')

# Bar Plot for Performance Metrics
fig3 = go.Figure()
for metric in metrics:
    fig3.add_trace(go.Bar(x=models, y=df[metric], name=metric))
fig3.update_layout(title='Performance Metrics for Each Model', xaxis_title='Model', yaxis_title='Metric Value', barmode='group')

# Box Plot for Performance Metrics
fig4 = go.Figure()
for metric in metrics:
    fig4.add_trace(go.Box(y=df[metric], name=metric))
fig4.update_layout(title='Distribution of Performance Metrics', yaxis_title='Metric Value')

# Line Plot for Time Taken
fig5 = go.Figure()
fig5.add_trace(go.Scatter(x=models, y=df['TT (Sec)'], mode='lines+markers'))
fig5.update_layout(title='Time Taken for Each Model', xaxis_title='Model', yaxis_title='Time (Sec)')

# Display plots
fig1.show()
fig2.show()
fig3.show()
fig4.show()
fig5.show()