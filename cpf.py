# Autor: Lucas Inácio
# API - CPF

# Importar biblioteca
import requests

cpf = '48764470806'
url = f'https://api.cpfhub.io/cpf/{cpf}'
headers = {
    'x-api-key': '18511129b02f5ead78a7e93ceb4e7266530176fbf49221462f72580a4643cece',
    'Accept': 'application/json'
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)