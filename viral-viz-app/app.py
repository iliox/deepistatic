# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df_cov = pd.read_csv('./viral-mutation/results/cov/semantics/analyze_semantics_cov2rbd_bilstm_512.txt', delimiter = "\t")
df_flu = pd.read_csv('./viral-mutation/results/flu/semantics/analyze_semantics_flu_h3_bilstm_512.txt', delimiter = "\t")
df_hiv = pd.read_csv('./viral-mutation/results/hiv/semantics/analyze_semantics_hiv_bilstm_512.txt', delimiter = "\t")

results = pd.read_csv('./viral-mutation/results/escape_results.txt', delimiter = "\t")

df_cov = df_cov.dropna()
df_flu = df_flu.dropna()
df_hiv = df_hiv.dropna()

df_cov['change'] = np.log(df_cov.change)
df_cov['prob'] = np.log(df_cov.prob)

df_flu['change'] = np.log(df_flu.change)
df_flu['prob'] = np.log(df_flu.prob)

df_hiv['change'] = np.log(df_hiv.change)
df_hiv['prob'] = np.log(df_hiv.prob)

fig1 = px.scatter(df_cov, x="prob", y="change", color="is_viable",
                    labels={
                     "prob": "Grammatically (fitness)",
                     "change": "Semantic Change"
                    },
                )

fig2 = px.scatter(df_cov, x="prob", y="change", color="is_escape",
                    labels={
                     "prob": "Grammatically (fitness)",
                     "change": "Semantic Change"
                    },
                )

fig3 = px.scatter(df_flu, x="prob", y="change", color="is_viable",
                    labels={
                     "prob": "Grammatically (fitness)",
                     "change": "Semantic Change"
                    },
                )

fig4 = px.scatter(df_flu, x="prob", y="change", color="is_escape",
                    labels={
                     "prob": "Grammatically (fitness)",
                     "change": "Semantic Change"
                    },
                )

fig5 = px.scatter(df_hiv, x="prob", y="change", color="is_viable",
                    labels={
                     "prob": "Grammatically (fitness)",
                     "change": "Semantic Change"
                    },
                )

fig6 = px.scatter(df_hiv, x="prob", y="change", color="is_escape",
                    labels={
                     "prob": "Grammatically (fitness)",
                     "change": "Semantic Change"
                    },
                )

fig7 = px.bar(results, x='Model', y='Escape AUC (Influenza A H1)')
fig8 = px.bar(results, x='Model', y='Escape AUC (Influenza A H3)')
fig9 = px.bar(results, x='Model', y='Escape AUC (HIV-1 Env BG505)')
fig10 = px.bar(results, x='Model', y='Escape AUC (SARS-CoV-2)')

app.layout = dbc.Container(
    [
        html.Center(html.H1(children='Mutation Vizualization Tool')),
        html.Center(html.Div(children='''
            A web application to check to mutation effects on viral protein.
        ''')),
        html.Br(),
        html.Hr(),
        html.Center(html.H2(children='SARS-CoV-2')),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='graph1',figure=fig1), md=6),
                dbc.Col(dcc.Graph(id='graph2',figure=fig2), md=6),
            ],
            align="center",
        ),
        html.Hr(),
        html.Center(html.H2(children='Influenza')),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='graph3',figure=fig3), md=6),
                dbc.Col(dcc.Graph(id='graph4',figure=fig4), md=6),
            ],
            align="center",
        ),
        html.Hr(),
        html.Center(html.H2(children='HIV Env')),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='graph5',figure=fig5), md=6),
                dbc.Col(dcc.Graph(id='graph6',figure=fig6), md=6),
            ],
            align="center",
        ),
        html.Hr(),
        html.Center(html.H2(children='Escape Results AUC')),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='graph7',figure=fig7), md=6),
                dbc.Col(dcc.Graph(id='graph8',figure=fig8), md=6),
            ],
            align="center",
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='graph9',figure=fig9), md=6),
                dbc.Col(dcc.Graph(id='graph10',figure=fig10), md=6),
            ],
            align="center",
        ),
    ],
    fluid=True,
)

if __name__ == '__main__':
    app.run_server(debug=True)
