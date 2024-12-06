import streamlit as st
import pydeck as pdk
import pandas as pd

# Carregar os dados do CSV
csv_file = 'anexo.csv'  # Substitua pelo caminho do seu arquivo CSV
data = pd.read_csv(csv_file, sep=';')

# Converter as colunas de Latitude e Longitude para o formato numérico correto
data['Latitude'] = data['Latitude'].str.replace(',', '.').astype(float)
data['Longitude'] = data['Longitude'].str.replace(',', '.').astype(float)

# Exibir os dados na interface
# st.write("Dados do CSV:", data)

# Configurar o mapa usando Pydeck
layer = pdk.Layer(
    "ScatterplotLayer",
    data=data,
    get_position=["Longitude", "Latitude"],
    get_color="[200, 30, 0, 160]",  # Cor dos pontos
    get_radius=5,  # Tamanho dos pontos
)

# Configuração inicial do mapa
view_state = pdk.ViewState(
    latitude=-23.5489,  # Latitude de Itapevi
    longitude=-46.9322, # Longitude de Itapevi
    zoom=23,
    
)

# Exibir o mapa
mapa = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    map_style='mapbox://styles/mapbox/light-v10',
    tooltip={"text": "Projeto: {N°. Projeto}\nLogradouro: {Logradouro}"}
)

st.pydeck_chart(mapa, use_container_width=True)
