import requests
import json
import csv

apikey = 'H210P55NPUWHP8HN'
outputsize = 'full' #full ou compact
#function = 'TIME_SERIES_DAILY'
function = 'TIME_SERIES_DAILY_ADJUSTED'
symbol = 'PETR4.SA'

fileIn  = 'acoes.csv'
fileOut = 'joinOut.csv'

urlBase = 'https://www.alphavantage.co/query?'

'''
    {
    "Meta Data": {
        "1. Information": "Daily Time Series with Splits and Dividend Events",
        "2. Symbol": "PETR4.SA",
        "3. Last Refreshed": "2018-04-12",
        "4. Output Size": "Compact",
        "5. Time Zone": "US/Eastern"
    },
    "Time Series (Daily)": {
        "2018-04-12": {
            "1. open": "21.7900",
            "2. high": "21.9400",
            "3. low": "21.6800",
            "4. close": "21.6800",
            "5. adjusted close": "21.6800",
            "6. volume": "36147600",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0000"
        }
'''             

def trata_retorno( data ):
    resultado = json.loads(data)
    
    lbSymbol = '2. Symbol'
    lbOpen   = '1. open'
    lbClose  = '4. close'
    lbLow    = '3. low'
    lbHigh   = '2. high'
    lbVolume = '6. volume'
    
    if resultado is not None:
        
        acao =''
        if 'Meta Data' in resultado:
            acao = (resultado['Meta Data'])[lbSymbol]

        if 'Time Series (Daily)' in resultado:
            with open(fileOut, 'a+', newline='') as fOut:
                 
                writer = csv.writer(fOut, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                
                for data, dados in resultado["Time Series (Daily)"].items():
    
                    if(lbOpen in dados):
                        open_   = dados[lbOpen]
                    
                    if(lbClose in dados):
                        close_  = dados[lbClose]
                    
                    if(lbLow in dados):
                        low_    = dados[lbLow]
                    
                    if(lbHigh in dados):
                        high_   = dados[lbHigh]
                    
                    if(lbVolume in dados):
                        volume_ = dados[lbVolume]
                    

                    writer.writerow([acao, data, open_, close_, low_, high_, volume_])
            
            fOut.close()

        else:
            print('Erro - {0}'.format(resultado))


'   ----------------- Logica Principal -------------------    '


with open(fileIn, 'r', newline='') as fIn:
            reader = csv.reader(fIn, delimiter=',', quotechar='"')
            for row in reader:
                if(row):
                    if(row[1] != ""):
                        symbol = row[0]
                        print ('Processando {0}'.format(symbol))


                        url = urlBase
                        url = '{0}function={1}'.format(url, function)
                        url = '{0}&apikey={1}'.format(url, apikey)
                        url = '{0}&outputsize={1}'.format(url, outputsize)
                        url = '{0}&symbol={1}'.format(url, symbol)

                        print(url)

                        r = requests.get(url)
                        
                        if (r.status_code == 200):
                            print('Retorno = {0}'.format(r.status_code))
                            trata_retorno(r.content.decode('utf-8'))
                            #print(r.content)
                        else:
                            print('Erro de conexao - {0}'.format(r.status_code))


print('FIM PROCESSAMENTO ... ')