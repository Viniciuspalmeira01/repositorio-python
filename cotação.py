import requests 


def obter_cotacao_moeda(moeda_origem, moeda_destino):
    url = f"https://api.exchangerate-api.com/v4/latest/{moeda_origem}"
    resposta = requests.get(url)
    
    if resposta.status_code != 200:
        raise Exception("Erro ao obter dados da API de câmbio.")
    
    dados = resposta.json()
    
    if moeda_destino not in dados['rates']:
        raise Exception(f"Moeda destino '{moeda_destino}' não encontrada.")
    
    taxa_cambio = dados['rates'][moeda_destino]
    return taxa_cambio

if __name__ == "__main__":
    moeda_origem = "USD"
    moeda_destino = "BRL"
    
    try:
        taxa = obter_cotacao_moeda(moeda_origem, moeda_destino)
        print(f"A cotação de {moeda_origem} para {moeda_destino} é: {taxa}")
    except Exception as e:
        print(f"Erro: {e}")
