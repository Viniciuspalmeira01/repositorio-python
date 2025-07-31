import pandas as pd
import matplotlib.pyplot as plt


vendas = {"data": ["01/01/2023", "02/01/2023", "03/01/2023", "04/01/2023"],
         "valor" : [100, 230 , 45 , 25],
         "produto": ["Produto A", "Produto B", "Produto C", "Produto D"],}
vendas_df = pd.DataFrame(vendas)

vendas_janeiro = {"Produtos": ["Produto A", "Produto B", "Produto C"],
                 "Valor unit" : [10 , 20 , 14],
                 "Unit.Vendidas": [10, 11, 6]}

vendas_janeiro_df = pd.DataFrame(vendas_janeiro)

#função que soma os valores das vendas do mês de Janeiro
def calcular_total_vendas(vendas_df):
    return vendas_df.loc[:,'Vendas'].sum()

#gráficos de barras com os valores das vendas

categorias =vendas_janeiro_df.loc[:, "Produtos"]
vendas_janeiro_df["Total"] = vendas_janeiro_df["Valor unit"] * vendas_janeiro_df["Unit.Vendidas"]
valores = vendas_janeiro_df.loc[:,"Total"] 

#desenho do gráfico
plt.figure(figsize=(8, 6))
plt.bar(categorias, valores, color='skyblue')
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.title('Gráfico de valores recebidos por produto ')
plt.grid(axis='y', linestyle='--')  # Grade apenas no eixo y
plt.show()
