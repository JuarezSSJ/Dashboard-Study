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

# Filtro por período
periodos = sorted(base["Ano-Mes"].unique())
periodo_selecionado = st.sidebar.selectbox("Selecione o Período:", periodos)

# Filtro por produto
produtos = sorted(base["Produto"].unique())
produto_selecionado = st.sidebar.multiselect("Selecione os Produtos:", produtos, default=produtos)

# Aplicar filtros
base_filtrada = base[
    (base["Ano-Mes"] == periodo_selecionado) &
    (base["Produto"].isin(produto_selecionado))
]

# Exibir dados filtrados
st.subheader("📋 Visualização da Tabela de Vendas Filtrada")
st.dataframe(base_filtrada)
