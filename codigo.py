import pandas as pd
import plotly.express as px
from IPython.display import display
import plotly.io as pio

# Configuração para abrir gráficos no navegador
pio.renderers.default = "browser"

# --- Importação e preparação da base ---
tabela = pd.read_csv('produtos_loja.csv')

display(tabela)  # Mostra a tabela
tabela.info()    # Mostra informações da tabela

# Remove linhas com valores nulos
tabela = tabela.dropna()

# Distribuição percentual por região
display(tabela["regiao"].value_counts(normalize=True))

# --- Quantidade vendida por produto ---
quantidade_produto = tabela.groupby("produto")["quantidade"].sum().sort_values(ascending=False)
display(quantidade_produto)

# --- Faturamento por produto ---
faturamento_produto = tabela.groupby("produto")["valor"].sum().sort_values(ascending=False)
display(faturamento_produto)

# Gráfico de faturamento por produto
grafico_produto = px.bar(
    faturamento_produto,
    x=faturamento_produto.index,
    y=faturamento_produto.values,
    title="Faturamento por Produto",
    labels={"x":"Produto", "y":"Faturamento (R$)"},
    text=faturamento_produto.values,
    color=faturamento_produto.index,
    color_discrete_sequence=px.colors.qualitative.Set2
)
grafico_produto.update_traces(textposition="outside")
grafico_produto.update_layout(template="plotly_white", title_font=dict(size=20), font=dict(size=14))
grafico_produto.show()

# --- Tratamento da coluna de data ---
tabela["data"] = pd.to_datetime(tabela["data"])
tabela["mes"] = tabela["data"].dt.month
tabela["ano"] = tabela["data"].dt.year

display(tabela.head())

# --- Faturamento por mês ---
faturamento_meses = tabela.groupby("mes")["valor"].sum().sort_values(ascending=False)
display(faturamento_meses)

grafico_temporal = px.line(
    faturamento_meses,
    x=faturamento_meses.index,
    y=faturamento_meses.values,
    title="Faturamento por Meses",
    markers=True,
    labels={"x":"Mês", "y":"Faturamento (R$)"}
)
grafico_temporal.update_layout(
    template="plotly_dark",
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=True, gridcolor="lightgrey"),
    title_font=dict(size=20, color="white"),
    font=dict(size=14, color="white")
)
grafico_temporal.show()

# --- Faturamento por região ---
faturamento_regiao = tabela.groupby("regiao")["valor"].sum().sort_values(ascending=False)

grafico_faturamento_regiao = px.bar(
    faturamento_regiao,
    x=faturamento_regiao.index,
    y=faturamento_regiao.values,
    title="Faturamento por Região",
    labels={"x":"Região", "y":"Faturamento (R$)"},
    text=faturamento_regiao.values,
    color=faturamento_regiao.index,
    color_discrete_sequence=px.colors.qualitative.Set2
)
grafico_faturamento_regiao.update_traces(textposition="outside")
grafico_faturamento_regiao.update_layout(template="plotly_white", title_font=dict(size=20), font=dict(size=14))
grafico_faturamento_regiao.show()

# --- Quantidade por região ---
quantidade_regiao = tabela.groupby("regiao")["quantidade"].sum().sort_values(ascending=False)

grafico_quantidade_regiao = px.bar(
    quantidade_regiao,
    x=quantidade_regiao.index,
    y=quantidade_regiao.values,
    title="Quantidade Vendida por Região",
    labels={"x":"Região", "y":"Quantidade"},
    text=quantidade_regiao.values,
    color=quantidade_regiao.index,
    color_discrete_sequence=px.colors.qualitative.Pastel
)
grafico_quantidade_regiao.update_traces(textposition="outside")
grafico_quantidade_regiao.update_layout(template="plotly_white", title_font=dict(size=20), font=dict(size=14))
grafico_quantidade_regiao.show()

# Exibir os Top 5 mais vendidos
top5_quantidade = quantidade_produto.head(5)
display(top5_quantidade)

# Gráfico dos Top 5 mais vendidos
grafico_top5_quantidade = px.bar(
    top5_quantidade,
    x=top5_quantidade.index,
    y=top5_quantidade.values,
    title="Top 5 Produtos Mais Vendidos",
    labels={"x":"Produto", "y":"Quantidade Vendida"},
    text=top5_quantidade.values,
    color=top5_quantidade.index,
    color_discrete_sequence=px.colors.qualitative.Set2
)
grafico_top5_quantidade.update_traces(textposition="outside")
grafico_top5_quantidade.update_layout(template="plotly_white", title_font=dict(size=20), font=dict(size=14))
grafico_top5_quantidade.show()