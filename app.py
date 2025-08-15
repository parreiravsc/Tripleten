import pandas as pd
import plotly.express as px
import scipy.stats
import streamlit as st

from TratamentoDados import DataFrame


# ler o conjunto de dados:
car_data = pd.read_csv(
    'C:\\Users\\vinyc\\Repositorios\\Tripleten\\vehicles.csv')  # lendo os dados

st.header('Infomações sobre vendas de carro 2018-2019 ')

# aplicando tratamento de dados no dataframe
tratar_df = DataFrame(car_data)
car_data = tratar_df.ajusta_dados()


# atribuir filtros:
# filtro de modelo
lista_modelos = car_data['model'].unique()
modelo_escolhido = st.selectbox('Selecione o modelo', lista_modelos)
# filtro de ano do modelo
anos_modelo = car_data['model_year'].sort_values().unique()
ano_selecionado = st.selectbox(
    'Selecione o ano do modelo desejado', anos_modelo)


# conjunto de dados filtrados
car_data_filt = car_data[
    (car_data['model'] == modelo_escolhido) &
    (car_data['model_year'] == ano_selecionado)
]


# selecionando a caracteristica de busca
carac_busca = st.selectbox('Selecione a característica de busca',
                           car_data_filt.columns[~car_data_filt.columns.isin(['model', 'model_year'])])

hist_button = st.button('Criar histograma')

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    st.write(f'{modelo_escolhido} - {ano_selecionado}')
    # criar um histograma
    fig = px.histogram(car_data_filt, x=carac_busca)


disp_button = st.button('Criar gráfico de dispersão pelo preço')
if disp_button:  # se o botão for clicado

    # escrever uma mensagem
    st.write(
        'Criando um gráfico de dispersão para os parametros de busca em relação ao preço')
    fig = px.scatter(car_data_filt, x=carac_busca, y="price")

    # exibir um gráfico de dispersão Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# if 'experiment_no' not in st.session_state:
#     st.session_state['experiment_no'] = 0

# if 'df_experiment_results' not in st.session_state:
#     st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no', 'iterations', 'mean'])


# chart = st.line_chart([0.5])

# def toss_coin(n):

#     trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

#     mean = None
#     outcome_no = 0
#     outcome_1_count = 0

#     for r in trial_outcomes:
#         outcome_no +=1
#         if r == 1:
#             outcome_1_count += 1
#         mean = outcome_1_count / outcome_no
#         chart.add_rows([mean])
#         time.sleep(0.05)

#     return mean

# number_of_trials = st.slider('Número de tentativas?', 1, 1000, 10)
# start_button = st.button('Executar')

# if start_button:
#     st.write(f'Executando o experimento de {number_of_trials} tentativas.')
#     st.session_state['experiment_no'] += 1
#     mean = toss_coin(number_of_trials)
#     st.session_state['df_experiment_results'] = pd.concat([
#         st.session_state['df_experiment_results'],
#         pd.DataFrame(data=[[st.session_state['experiment_no'],
#                             number_of_trials,
#                             mean]],
#                      columns=['no', 'iterations', 'mean'])
#         ],
#         axis=0)
#     st.session_state['df_experiment_results'] = \
#         st.session_state['df_experiment_results'].reset_index(drop=True)

# st.write(st.session_state['df_experiment_results'])
