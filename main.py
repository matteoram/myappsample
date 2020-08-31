import requests as rq

response = requests.get('https://api.ultimate-dimensions.net/covid/stats/3E7EC19382E0EB488F90A87807BA998EF5B1FD7C50D181999763FC5D921BE41D/2020-08-23')

data = response.json

print(data)