import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import pandas as pd
from dash.dependencies import Input, Output


import io
import pandas as pd
import json
import os



# Load data
df = pd.read_excel("data/prepared_covid_data.xlsx")



# Initialize the app
app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True


def get_options(list_countriesAndTerritoriess):
    dict_list = []
    for i in list_countriesAndTerritoriess:
        dict_list.append({'label': i, 'value': i})

    return dict_list


app.layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                    html.Div(className='four columns div-user-controls',
                             children=[
                                 html.H2('COVID-19 2020 Summary - By Amine Hosni @Quantylix'),
                                 html.P('Visualising Covid Data for 2020 with Plotly - Dash.'),
                                 html.P('Pick one or more countries from the dropdown below.'),
                                 html.Div(
                                     className='div-for-dropdown',
                                     children=[
                                         dcc.Dropdown(id='countriesAndTerritoriesselector', options=get_options(df['countriesAndTerritories'].unique()),
                                                      multi=True, 
                                                      # value=[df['countriesAndTerritories'].sort_values()[0]],
                                                      style={'backgroundColor': '#1E1E1E'},
                                                      # value='Tunisia',
                                                      className='countriesAndTerritoriesselector'
                                                      ),
                                         dcc.RadioItems(id="per_time_data",options=[
                                                        {'label': 'Daily', 'value': 'daily'},
                                                        {'label': '7 days', 'value': '7 days'},
                                                        {'label': '14 days', 'value': '14 days'},],
                                                        value='14 days',
                                                        style={'backgroundColor': '#1E1E1E','color':'#d8d8d8'},
                                                        className='countriesAndTerritoriesselector'
                                                    ),
                                         dcc.RadioItems(id="absolute_per_population",options=[
                                                        {'label': 'Per 100k habitants', 'value': 'per 100k habitants'},
                                                        {'label': 'Absolute cases', 'value': 'absolute'}],
                                                        value='per 100k habitants',
                                                        style={'backgroundColor': '#1E1E1E','color':'#d8d8d8'},
                                                        className='countriesAndTerritoriesselector'
                                                    ),
                                     ],
                                     style={'color': '#1E1E1E'})
                                ]
                             ),

                    html.Div(className='eight columns div-for-charts bg-grey',
                             children=[
                                 dcc.Graph(id='timeseries', config={'displayModeBar': False}),
                                 dcc.Graph(id='timeseries2', config={'displayModeBar': False})

                             ])
                              ])
        ]

)


# Callback for timeseries price
@app.callback(Output('timeseries', 'figure'),
              Input('countriesAndTerritoriesselector', 'value'),
              Input('per_time_data','value'),
              Input('absolute_per_population','value'))

def update_graph(selected_dropdown_value, per_time_data, absolute_per_population):
    # print(per_time_data)
    trace1 = []
    df_sub = df

    if per_time_data == 'daily':
      target_col = 'tot_cases'

    if per_time_data == '7 days':
      if absolute_per_population == 'absolute':

        target_col = 'cum_cases_7_days'
      elif absolute_per_population == 'per 100k habitants':

        target_col = 'cum_cases_7_days_per_100k_population'
    if per_time_data == '14 days':
      if absolute_per_population == 'absolute':

        target_col = 'cum_cases_14_days'
      elif absolute_per_population == 'per 100k habitants':

        target_col = 'Cumulative_number_for_14_days_of_COVID-19_cases_per_100000'



    for countriesAndTerritories in selected_dropdown_value:
        trace1.append(go.Scatter(x=df_sub[df_sub['countriesAndTerritories'] == countriesAndTerritories].dateRep,
                                 y=df_sub[df_sub['countriesAndTerritories'] == countriesAndTerritories][target_col],
                                 mode='lines',
                                 opacity=0.7,
                                 name=countriesAndTerritories,
                                 textposition='bottom center'))
    traces = [trace1]
    data = [val for sublist in traces for val in sublist]
    figure = {'data': data,
              'layout': go.Layout(
                  colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  margin={'b': 15},
                  height=300,
                  hovermode='x',
                  autosize=True,
                  title={'text': 'Cumulative new cases for' + per_time_data + ' ' +absolute_per_population, 'font': {'color': 'white'}, 'x': 0.5},
                  yaxis={'range': [df_sub[df_sub['countriesAndTerritories'].isin(selected_dropdown_value)][target_col].min(),
                                  df_sub[df_sub['countriesAndTerritories'].isin(selected_dropdown_value)][target_col].max()]},
              ),

              }

    return figure

@app.callback(Output('timeseries2', 'figure'),
              Input('countriesAndTerritoriesselector', 'value'),
              Input('per_time_data','value'),
              Input('absolute_per_population','value'))
def update_graph(selected_dropdown_value, per_time_data, absolute_per_population):
    trace1 = []
    df_sub = df

    if per_time_data == 'daily':
      target_col = 'tot_deaths'

    if per_time_data == '7 days':
      if absolute_per_population == 'absolute':

        target_col = 'cum_deaths_7_days'
      elif absolute_per_population == 'per 100k habitants':

        target_col = 'cum_deaths_7_days_per_100k_population'
    if per_time_data == '14 days':
      if absolute_per_population == 'absolute':

        target_col = 'cum_deaths_14_days'
      elif absolute_per_population == 'per 100k habitants':

        target_col = 'cum_deaths_14_days_per_100k_population'
    for countriesAndTerritories in selected_dropdown_value:
        trace1.append(go.Scatter(x=df_sub[df_sub['countriesAndTerritories'] == countriesAndTerritories].dateRep,
                                 y=df_sub[df_sub['countriesAndTerritories'] == countriesAndTerritories][target_col],
                                 mode='lines',
                                 opacity=0.7,
                                 name=countriesAndTerritories,
                                 textposition='bottom center'))
    traces = [trace1]
    data = [val for sublist in traces for val in sublist]
    figure = {'data': data,
              'layout': go.Layout(
                  colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  margin={'b': 15},
                  height=300,
                  hovermode='x',
                  autosize=True,
                  title={'text': 'Cumulative new deaths for' + per_time_data + ' ' +absolute_per_population, 'font': {'color': 'white'}, 'x': 0.5},
                  yaxis={'range': [df_sub[df_sub['countriesAndTerritories'].isin(selected_dropdown_value)][target_col].min(),
                                  df_sub[df_sub['countriesAndTerritories'].isin(selected_dropdown_value)][target_col].max()]},
              ),

              }

    return figure


if __name__ == '__main__':
    app.run_server(debug=False)