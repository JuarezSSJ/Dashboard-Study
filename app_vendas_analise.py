import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

st.title("📊 Análise de Vendas")
st.write("Bem-vindo ao seu primeiro app com Streamlit! 🚀")

# Carregar dados
base = pd.read_csv("vendas.csv")
base["Data"] = pd.to_datetime(base["Data"])
base["Ano-Mes"] = base["Data"].dt.to_period("M").astype(str)

# Sidebar com filtros
st.sidebar.header("🔎 Filtros")

#filtro período
periodo = sorted(base["Ano-Mes"].unique())
periodo_selecionado = st.sidebar.selectbox("Selecione o Período:", periodo)

#filtro de categorias
categorias = sorted(base["Categoria"].unique())
categorias_selecionadas = st.sidebar.multiselect("Escolha as categorias:",categorias)

# Aplicar filtros
base_filtrada = base[
    (base["Ano-Mes"] == periodo_selecionado) &
    (base["Categoria"].isin(categorias_selecionadas))
]

# Exibir dados filtrados
st.subheader("📋 Visualização da Tabela de Vendas Filtrada")
st.dataframe(base_filtrada)