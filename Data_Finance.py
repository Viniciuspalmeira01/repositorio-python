import pandas as pd
import yfinance as yf
import pandas_datareader.data as pdr
import matplotlib.pyplot as plt
import datetime as dt
from time import sleep


class Finance:
    def __init__(self, ativos: list, start_date:str, end_date:str):
        self.ativos = ativos
        self.start_date = start_date
        self.end_date = end_date

    def get_ticker(self):
        print(f"Buscando cotações de: {', '.join(self.ativos)}")
        print(f"Período: {self.start_date} até {self.end_date}")
        dados_multiplos_ativos = yf.download(
         self.ativos,
         start=self.start_date,
         end=self.end_date,
         interval="1d"  #'1d' para dados diários
        )
        return dados_multiplos_ativos


    def exebition(self, data:pd.DataFrame):
        print("\n--- Dados Históricos Brutos (Cabeçalho) ---")
        print(data.head())

    def get_close(self, data:pd.DataFrame):
        closing_prices = data['Adj Close'].dropna()
        closing_prices.columns = [col.replace(".SA", "") for col in closing_prices.columns]
        closing_prices.rename(columns={'^BVSP': 'IBOV'}, inplace=True)
        return closing_prices


#A definição dos parametros das funções
lista_ativos = ['PETR4.SA', 'VALE3.SA', 'ITUB4.SA', 'B3SA3.SA', '^BVSP']
time_start = "2023-01-01"
time_end = dt.date.today().strftime("%Y-%m-%d")
info_finance = Finance(lista_ativos ,time_start, time_end )

#execução do código
dados = info_finance.get_ticker()
info_finance.exebition(dados)
precos_fechamento = info_finance.get_close(dados)
