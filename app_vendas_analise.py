import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

st.title("📊 Análise de Vendas")
st.write("Bem-vindo ao seu primeiro app com Streamlit! 🚀")

# Carregar dados
base = pd.read_csv("vendas.csv")
base["Data"] = pd.to_datetime(base["Data"])
base["Ano-Mes"] = base["Data"].dt.to_period("M").astype(str)

# Sidebar com filtros
st.sidebar.header("🔎 Filtros")
categorias = st.sidebar.multiselect(
    "Selecione as Categorias:",
    options=base["Categoria"].unique(),
    default=base["Categoria"].unique()  # Todas selecionadas por padrão
)

periodos = st.sidebar.multiselect(
    "Selecione os Períodos:",
    options=sorted(base["Ano-Mes"].unique()),
    default=sorted(base["Ano-Mes"].unique())[:3]  # 3 mais recentes por padrão
)

# Aplicar filtros
base_filtrada = base[
    (base["Categoria"].isin(categorias)) &
    (base["Ano-Mes"].isin(periodos))
]

# Pré-processamento CRUCIAL: Criar tabela dinâmica
dados_grafico = base_filtrada.pivot_table(
    index="Categoria",         # Eixo Y
    columns="Ano-Mes",         # Eixo X 
    values="Valor Total",      # Valores
    aggfunc="sum"              # Soma os valores
).fillna(0)

st.subheader("📊 Vendas por Categoria e Período")

# Opção 1: Gráfico de barras empilhadas (Streamlit)
st.bar_chart(dados_grafico)
