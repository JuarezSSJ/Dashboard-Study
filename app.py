import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st
import pandas as pd

st.title("Meu Primeiro Dashboard com Streamlit")

df = pd.read_csv("vendas.csv")
st.write("Visualizando os dados:")
st.dataframe(df)

st.write("Resumo por produto:")
resumo = df.groupby("Produto")[["Quantidade", "Valor Total"]].sum()
st.dataframe(resumo)