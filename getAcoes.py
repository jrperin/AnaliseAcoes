import json


api_token = 'your_api_token'
api_url_base = 'https://api.digitalocean.com/v2/'

#api_url_base = 'https://www.alphavantage.co/query?apikey=H210P55NPUWHP8HN&function=TIME_SERIES_DAILY_ADJUSTED&outputsize=full&symbol='
api_url_base = 'https://www.alphavantage.co/query?apikey=H210P55NPUWHP8HN&function=TIME_SERIES_DAILY_ADJUSTED&symbol='
headers = {'Content-Type': 'application/json'}

api_url = '{0}PETR4.SA'.format(api_url_base)
print(api_url)

response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    resultado = json.loads(response.content.decode('utf-8'))
    if resultado is not None:
        print("Here's your info: ")
        for data, dados in resultado["Time Series (Daily)"].items():
            # print('data = {0}'.format(dados))
            open_  = dados['1. open']
            close_ = dados['4. close']
            print('{0} -> {1}, {2}'.format(data, open_, close_))
            #for descr, valor in dados.items():
            #    print('{0}, {1}'.format(descr, valor))

        else:
            print('[!] Request Failed')
else:
    print("Erro")






#https://www.alphavantage.co/query?apikey=H210P55NPUWHP8HN&function=TIME_SERIES_DAILY&symbol=MSFT&outputsize=full
#https://www.alphavantage.co/query?apikey=H210P55NPUWHP8HN&function=TIME_SERIES_DAILY_ADJUSTED&outputsize=full&symbol=ITUB4
