import pandas as pd 
import os 
import matplotlib.pyplot as plt
from customtkinter import *

from time import sleep


class Reader_csv: 
    def __init__(self, caminho:str):
        self.caminho =  caminho
        self.meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "Outubro", "novembro","dezembro"]
        self.trimestre = {"Trimestre 1": ["janeiro", "fevereiro", "março"],
                          "Trimestre 2": ["abril", "maio", "junho"],
                          "Trimestre 3": ["julho", "agosto", "setembro"],}
        

    def ler_planilha(self, aba:int = 1) ->None:
        if not os.path.isfile(self.caminho):
            print("Isso não é um arquivo")
        else:
             print("Arquivo encontrado com sucesso")
             df = pd.read_excel(self.caminho, sheet_name=aba)
             return df.head()

    def apresentar_faturamento(self,caminho:str , aba: int = 1,) ->None:
        vendas_df = pd.read_excel(caminho, aba)
        soma = vendas_df["Faturamento"].sum()
        return soma


    def data_analise(self, faturamento : int , meta: int) ->None: #Analise mensal e trimestral
        
        #analise do trimestre:
        for chave in self.trimestre:
            faturamento_trimestre = 0
            for mes in self.trimestre[chave]:
                if os.path.isfile(f"vendas-{mes}.xlsx"):
                    faturamento_trimestre += self.apresentar_faturamento(f"vendas-{mes}.xlsx")
                else:
                    print(f"Arquivo do mês de {mes} não encontrado.")
            return (f"O faturamento do {chave} foi de: R$ {faturamento_trimestre:.2f}")
        
        
        
    #criando os gráficos de barras:
    def grafico_barras(self):   
        meses = [] #lista para armazenar os meses com arquivos existentes
        faturamentos = [] #lista para armazenar os faturamentos mensais
        soma_tri = 0
        for mes in self.meses:
            if os.path.isfile(f"vendas-{mes}.xlsx"):
                meses.append(mes)
                faturamentos.append(self.apresentar_faturamento(f"vendas-{mes}.xlsx"))
                soma_tri = sum(faturamentos)

            else: 
                print(f"Arquivo do mês de {mes} não encontrado, pulando para o próximo mês.")

        plt.bar("trimestre", soma_tri)
        plt.xlabel("Trimestre")
        plt.ylabel("Faturamento (R$)")
        plt.title("Faturamento Mensal")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


class Frame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(fill="both", expand=True)

class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("Análise de Vendas")
        self.geometry("1200x600")

        self.label = CTkLabel(self, text="Análise de Vendas Mensal e Trimestral")
        self.label.pack(pady=20)

        self.button = CTkButton(self, text="Iniciar Análise", command=self.iniciar_analise, corner_radius=32, fg_color="#1f6aa5", hover_color="#367fa9")
        self.button.pack(pady=10)

        self.frm = Frame(self)
        self.frm.pack(pady=20, padx=20, fill="both", expand=True)

    def iniciar_analise(self):
        #Iniciando a análise
        red = Reader_csv("vendas-janeiro.xlsx")
        faturamento = red.apresentar_faturamento("vendas-janeiro.xlsx")
        resultado_analise = red.data_analise(faturamento, 6000)

        resultado_label = CTkLabel(self.frm, text=f"Faturamento: R$ {faturamento:.2f}\n{resultado_analise}")
        resultado_label.pack(pady=10)

        sleep(3) #dando tempo para o usuário ler o resultado
        red.grafico_barras()
        
app = App()
app.mainloop()
#exemplo de uso:
"""red = Reader_csv("vendas-janeiro.xlsx")
#print(red.apresentar_faturamento("vendas-janeiro.xlsx"))
print(red.data_analise(50000, 6000))
red.grafico_barras()"""
