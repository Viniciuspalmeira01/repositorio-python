from nwe import db , perfil , Moedas
from datetime import datetime
import requests
import matplotlib.pyplot as plt
import seaborn as sns

db.connect()
db.create_tables([perfil , Moedas])

class Cotações:
          def __init__(self) -> None:
                  self.horario = datetime.now().strftime('%H:%M')
                  
          def get_exchange_rate(self, api_key ,moeda_base , siglas):
                     url = f"https://open.er-api.com/v6/latest/{moeda_base}" 
                     response = requests.get(url)  
                     data = response.json()
                     if response.status_code == 200 and 'rates' in data:
                        return data['rates'].get(siglas, None)
                     else:
                       raise Exception("Erro na busca da cotação")
          def cripto(self, nome , brl = 'BRL'):
                    url = f"https://api.coingecko.com/api/v3/simple/price?ids={nome}&vs_currencies=usd"
                    response = requests.get(url)
                    data = response.json()
                    if response.status_code == 200:
                              return data.get(nome, {}).get('usd', None)
                    else:
                              raise Exception("Erro na busca da cotação da cripto")
                    
          def run(self):
            lista_moedas = ['USD', 'EUR', 'ARS', 'JPY', 'GBP']
            nomes_moedas = ['Dolar', 'Euro', 'Peso', 'Iene']
            api_key = 'YOUR_API_KEY'
            resultados = []

            try:
              for sigla, nome in zip(lista_moedas, nomes_moedas):
                resultado = self.get_exchange_rate(api_key, moeda_base=sigla, siglas='BRL')
                resultados.append(f"Taxa de câmbio às {self.horario} do {nome} (BRL): {resultado}")
                return resultados
            except Exception as e:
                  print(f'Erro no código: {e}')
            
          def criar_grafico(self,dados):
               moedas, valores = zip(*dados)
               plt.figure(figsize=(10, 6))
               sns.barplot(x=moedas, y=valores)
    
               plt.title('Taxas de Câmbio em Relação ao Real (BRL)')
               plt.xlabel('Moeda')
               plt.ylabel('Valor em BRL')
               plt.show()

class Banco:
      def __init__(self, name , idade , email , senha) -> None:#Inicia define parâmetros para outros métodos
            self.name = name 
            self.idade = idade
            self.email = email #Chave induplicável 
            self. senha = senha
      
      def criar_perfil(self):
        usuario = perfil.create(name=self.name, email=self.email, senha=self.senha)
        return usuario

      def integração(self):
        usuario = self.criar_perfil()
        cotações = Cotações()
        valores = cotações.run()

        for valor in valores:
            Moedas.create(
                nome=usuario,
                Horário=datetime.now(),  # Melhor pegar a hora atual aqui
                valor_atualizado=valor
            )

cotações = Cotações()
dados = cotações.Run()
cotações.criar_grafico(dados)