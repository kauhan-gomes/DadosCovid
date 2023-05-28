# -*- coding: utf-8 -*-

import pandas as pd
import plotly.express as px
import streamlit as st

#streamlit run codigoBase.py

#LENDO O DATASET
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

#MELHORANDO O NOME DAS COLUNAS DA TABELA
df = df.rename(columns={'newDeaths': 'Novos óbitos', 'newCases': 'Novos casos', 'deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes', 'totalCases_per_100k_inhabitants': 'Casos por 100 mil habitantes'})

#SELECÃO DO ESTADO
estados = list(df['state'].unique())
state = st.selectbox('Qual o estado desejado?', estados)

#SELEÇÃO DO GRÁFICO
graficos = ['Gráfico de Linha', 'Gráfico de Barras', 'Gráfico de Dispersão']
grafico = st.selectbox('Qual tipo de gráfico?', graficos)

#SELEÇÃO DA COLUNA
colunas = ['Novos óbitos', 'Novos casos', 'Óbitos por 100 mil habitantes', 'Casos por 100 mil habitantes']
column = st.selectbox('Qual tipo de informação?', colunas)

#SELEÇÃO DAS LINHAS QUE PERTECEM AO ESTADO
df = df[df['state'] == state]

if grafico == 'Gráfico de Linha':
    fig = px.line(df, x="date", y=column, title=column + ' - ' + state)
elif grafico == 'Gráfico de Barras':
    fig = px.bar(df, x="date", y=column, title=column + ' - ' + state)
else:
    fig = px.scatter(df, x="date", y=column, title=column + ' - ' + state)

fig.update_layout(xaxis_title='Data', yaxis_title=column.upper(), title={'x': 0.5})

st.title('DADOS COVID - BRASIL')
st.write('Nessa aplicação, o usuário tem a opção de escolher o estado, o tipo de gráfico e o tipo de informação para mostrar o gráfico. Utilize o menu lateral para fazer as escolhas.')

st.plotly_chart(fig, use_container_width=True)

st.caption('Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br')
