import pandas as pd
import plotly.express as px
from IPython.display import display
import plotly.io as pio
pio.renderers.default = "browser"


tabela = pd.read_csv('produtos_loja.csv')

display(tabela)#Mostra a tabela formalizada

tabela.info() #Mostra informações da tabela como tipos de dados

tabela = tabela.dropna ()# Dropamos tcolunas vazias

display(tabela["regiao"].value_counts(normalize=True) ) #Mostramos em forma de porcentagem selecionando a coluna região e contando a quantidade de vendas por região 

for coluna in tabela.columns: #Declaramos um loop que percorre todas as linhas e colunas e vão ter base em produtos ou qualquer outra coluna
    grafico = px.histogram(tabela, x=coluna, color="produto", text_auto=True) #Mostram todas as colunas relaciuonadas a produtos e região 
    grafico.show()

# Quantidade vendida por produto
quantidade_produto = tabela.groupby("produto")["quantidade"].sum().sort_values(ascending=False)
display(quantidade_produto)

# Faturamento por produto
faturamento_produto = tabela.groupby("produto")["valor"].sum().sort_values(ascending=False)
display(faturamento_produto)

# Gráfico de barras do faturamento
grafico_produto = px.bar(faturamento_produto, x=faturamento_produto.index, y=faturamento_produto.values,
                         title="Faturamento por Produto")
grafico_produto.show()
#Transformação da coluna data para a ferramenta do panda date time que cria outras colunas a partir de uma data 
tabela["data"] = pd.to_datetime(tabela["data"])

tabela["mes"] = tabela["data"].dt.month

tabela["ano"] = tabela["data"].dt.year

display(tabela.head())
#Aqui temos agrupamento da coluna mes e depois somando todos os valores por mes ordenados em decrescente 
faturamento_meses = tabela.groupby("mes")["valor"].sum().sort_values(ascending=False)
display(faturamento_meses)

grafico_temporal = px.line(
    faturamento_meses,
    x=faturamento_meses.index,       # eixo X: meses
    y=faturamento_meses.values,      # eixo Y: faturamento
    title="Faturamento por Meses",   # título do gráfico
    markers=True,                    # adiciona bolinhas nos pontos
    labels={"x":"Mês", "y":"Faturamento (R$)"}, # rótulos dos eixos
)

# Ajustes visuais extras
grafico_temporal.update_layout(
    template="plotly_dark",          # estilo escuro moderno
    xaxis=dict(showgrid=False),      # remove grade do eixo X
    yaxis=dict(showgrid=True, gridcolor="lightgrey"), # grade suave no Y
    title_font=dict(size=20, color="white"),          # título maior e branco
    font=dict(size=14, color="white")                 # fonte geral
)

grafico_temporal.show()
