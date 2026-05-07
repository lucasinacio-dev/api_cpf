# Autor: Lucas Inácio
# API - CPF

# Importar biblioteca
import requests

cpf = '48764470806'
url = f'https://api.cpfhub.io/cpf/{cpf}'
headers = {
    'x-api-key': 'api-key',
    'Accept': 'application/json'
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)