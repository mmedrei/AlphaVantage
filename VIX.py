import requests
import pandas as pd
import numpy as np


ticker='VIX' # Define ticker
date='2025-02-27' # Define fecha
interest_rate=0.05 # Define tipo de interes

# Definir parametros de consulta
params ={"function": "SYMBOL_SEARCH",
         "apikey":"ZJI624HFWBESIXTB",
         "keywords":ticker}



# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=tesco&apikey=demo'
data= requests.get('https://www.alphavantage.co/query', params=params).json()

print(data)
# ------------------------
# -------example 3 ------------





# Definir parametros de consulta
params ={"function": "TIME_SERIES_DAILY",
         "outputsize":"compact",
         "apikey":"ZJI624HFWBESIXTB",
         "symbol":ticker}

# Obtener la respuesta
prices_raw=requests.get('https://www.alphavantage.co/query', params=params).json()

#Formatear datos
prices=pd.DataFrame(prices_raw['Time Series (Daily)']).T
prices.columns=['Open', 'High', 'Low', 'Close', 'Volume']
prices=prices.astype({'Open':'float', 'High':'float', 'Low':'float','Close':'float', 'Volume':'Int64'})
prices.index=pd.to_datetime(prices.index)
prices.sort_index(inplace=True)

# Mostrar 5 ultimos valores
print(prices.tail())