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

vendedores = st.sidebar.multiselect(
    "Selecione os Vendedores:",
    options=base["Vendedor"].unique(),
    default=base["Vendedor"].unique()
)

# Aplicar filtros
base_filtrada = base[
    (base["Categoria"].isin(categorias)) &
    (base["Ano-Mes"].isin(periodos))
]

base_filtrada_vendedor = base[
    (base["Categoria"].isin(categorias)) &
    (base["Ano-Mes"].isin(periodos)) &
    (base["Vendedor"].isin(vendedores))
]

# Pré-processamento CRUCIAL: Criar tabela dinâmica
dados_grafico = base_filtrada.pivot_table(
    index="Categoria",         # Eixo Y
    columns="Ano-Mes",         # Eixo X 
    values="Valor Total",      # Valores
    aggfunc="sum"              # Soma os valores
).fillna(0)

st.subheader("📊 Vendas por Categoria e Período")

#Gráfico de barras empilhadas (Streamlit)
st.bar_chart(dados_grafico)


dados_grafico_vendedor = base_filtrada_vendedor.pivot_table(
    index="Categoria",         # Eixo Y
    columns="Ano-Mes",         # Eixo X 
    values="Valor Total",      # Valores
    aggfunc="sum"              # Soma os valores
).fillna(0)

st.subheader("📊 Vendas por Categoria e Período e Vendedor")

st.bar_chart(dados_grafico_vendedor)

total_vendido = base_filtrada["Valor Total"].sum()
ticket_medio = total_vendido / base_filtrada["Quantidade"].sum()
produto_top = base_filtrada.groupby("Produto")["Quantidade"].sum().idxmax()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Vendido", f"R${total_vendido:,.2f}")
col2.metric("🧾 Ticket Médio", f"R${ticket_medio:,.2f}")
col3.metric("🥇 Produto + Vendido", produto_top)
