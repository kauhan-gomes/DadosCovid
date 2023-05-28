# -*- coding: utf-8 -*-

import pandas as pd
import plotly.express as px
import streamlit as st

# Lendo o dataset
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

# Melhorando o nome das colunas da tabela
df = df.rename(columns={'newDeaths': 'Novos óbitos', 'newCases': 'Novos casos', 'deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes', 'totalCases_per_100k_inhabitants': 'Casos por 100 mil habitantes'})

# Selecionando o estado
estados = list(df['state'].unique())
state = st.sidebar.selectbox('Selecione o estado', estados)

# Selecionando o tipo de informação
colunas = ['Novos óbitos', 'Novos casos', 'Óbitos por 100 mil habitantes', 'Casos por 100 mil habitantes']
column = st.sidebar.selectbox('Selecione o tipo de informação', colunas)

# Selecionando o tipo de gráfico
tipos_grafico = ['Gráfico de Linha', 'Gráfico de Área', 'Gráfico de Barras']
tipo_grafico = st.sidebar.selectbox('Selecione o tipo de gráfico', tipos_grafico)

# Filtrando os dados do estado selecionado
df_estado = df[df['state'] == state]

# Criando o gráfico
if tipo_grafico == 'Gráfico de Linha':
    fig = px.line(df_estado, x='date', y=column, title=column + ' - ' + state)
elif tipo_grafico == 'Gráfico de Área':
    fig = px.area(df_estado, x='date', y=column, title=column + ' - ' + state)
else:
    fig = px.bar(df_estado, x='date', y=column, title=column + ' - ' + state)

# Personalizando o layout do gráfico
fig.update_layout(xaxis_title='Data', yaxis_title=column.upper(), title={'x': 0.5}, width=1500, height=800) # Aumentando a largura e altura do gráfico

# Exibindo o título e o gráfico no Streamlit
st.title('Dados COVID-19 - Brasil')
st.write('Este sistema permite visualizar gráficos interativos com dados da COVID-19 no Brasil.')

st.sidebar.markdown('---')
st.sidebar.caption('Selecione as opções no menu lateral para atualizar o gráfico.')

st.plotly_chart(fig, use_container_width=True)

# Rodapé
st.caption('Dados obtidos do repositório: https://github.com/wcota/covid19br')



