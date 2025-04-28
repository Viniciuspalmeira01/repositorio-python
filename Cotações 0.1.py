from nwe import db , perfil , Moedas
from datetime import datetime
import requests

db.connect()#Conexão com o banco
db.create_tables([perfil , Moedas])#Criação das tabelas 

#Criando o perfil que irá 
class Criar_perfil:
        def __init__(self) -> None:
                pass

        def perfil(self,name ,senha):
          resultado = perfil.create(nome = f'{name}', email = f'{name}@gmail.com', senha= f'{senha}').save()
          return resultado
        
        def Create(self):
                lista_de_nomes = ['Gustavo', 'Lucas' , 'Vinicius', 'Paulo']
                listas_senhas = ['12121' ,'21222' , '222323', '212121']
                for x in lista_de_nomes:
                        for _ in listas_senhas:
                                self.perfil(name=f'{x}', senha=_)

#Objeto que conecta a uma API, e busca as informações
class Cotação:
          def __init__(self):
                  self.api_key = 'YOUR API KEY'
                  self.moedas_sligas = ['USD', 'EUR', 'ARS']#siglas das moedas
                  self.moedas = ['dollar', 'Euro' , 'Peso']#moedas 
                  self.horario = datetime.now().time()
          
          def get_exchange_rate(self, base_currency, target_currency):
                    url = f"https://open.er-api.com/v6/latest/{base_currency}"
                    response = requests.get(url)
                    data = response.json()
                    if response.status_code == 200 and 'rates' in data:
                        return data['rates'].get(target_currency, None)
                    else:
                       raise Exception("Error fetching exchange rates")
          def get_crypto_price(self, crypto_id):
                    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
                    response = requests.get(url)
                    data = response.json()
                    if response.status_code == 200:
                              return data.get(crypto_id, {}).get('usd', None)
                    else:
                              raise Exception("Error fetching cryptocurrency price")
          
          def run(self):
                    resultados = []
                    for moeda, sigla in zip(self.moedas, self.moedas_sligas):
                              valor = self.get_exchange_rate(sigla, 'BRL')
                              resultado = f'Às {self.horario} a cotação do {moeda} é {valor}'
                              resultados.append(resultado)
                    return resultado
                  
class Banco:
         def __init__(self) -> None:
                    #self.perfil = perfil.get(perfil.nome == '')
                    pass
         def principal(self):
                    cotacao = Cotação()
                    resultados = cotacao.run()
                    for resultado in resultados:
                               Moedas.create(nome=self.perfil,
                                         valor_atualizado=resultado)

         def exibir(self, name, senha):
                    Criar_perfil().perfil(name=name, senha=senha)
                    lista_de_usuarios = perfil.select()
                    for usuario in lista_de_usuarios:
                              print(usuario)

#Banco().principal()
Banco().exibir('nome_do_usuário', 'senha_do_usuário')