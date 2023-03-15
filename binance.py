import json
import requests
import pandas as pd

# Defining Binance API URL
key = "https://api.binance.com/api/v3/ticker/price?symbol="
# Making list for multiple crypto's
currencies = ["BTCUSDT", "DOGEUSDT", "LTCUSDT"]
j = 0
  
# running loop to print all crypto prices
for i in currencies:
    
    # completing API for request
    url = key+currencies[j]  
    data = requests.get(url)
    data = data.json()
    print(data)
    j = j+1
    print(f"{data['symbol']} price is {data['price']}")
    
import requests

market = 'ETHEUR'
tick_interval = '1d'

url = 'https://api.binance.com/api/v3/klines?symbol='+market+'&interval='+tick_interval
data = requests.get(url).json()

#print(data)

import requests
import json
import pandas as pd

# Set up the Binance API endpoint
base_url = 'https://api.binance.com/api/v3/klines'

# Define the parameters for the request
symbol = ['BTCUSDT', 'ETHUSDT']  # List of symbols to retrieve
interval = '1d'  # Interval of klines data
limit = 1000  # Maximum number of klines data to retrieve

# Define a function to retrieve market cap data for a symbol
def get_market_cap_data(symbol):
    params = {'symbol': symbol, 'interval': interval, 'limit': limit}
    response = requests.get(base_url, params=params)
    klines = json.loads(response.text)
    df = pd.DataFrame(klines, columns=['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore'])
    df['Open time'] = pd.to_datetime(df['Open time'], unit='ms')
    df['Market cap'] = pd.to_numeric(df['Quote asset volume']) * pd.to_numeric(df['Close']) 
    df = df.set_index('Open time')
    return df['Market cap']

# Retrieve market cap data for all symbols
market_cap_data = {}
for s in symbol:
    market_cap_data[s] = get_market_cap_data(s)

# Merge the market cap data for all symbols into a single DataFrame
df_market_cap = pd.DataFrame(market_cap_data)
df_market_cap.index.name = 'Date'
df_market_cap = df_market_cap.loc[df_market_cap.index >= '2021-01-01']  # Filter by date range

# Print the resulting DataFrame
#print(df_market_cap)








import requests
from datetime import datetime, timedelta

# Spécifiez la plage de dates pour laquelle vous souhaitez calculer la capitalisation boursière historique
start_date = datetime(2022, 12, 30) # date de début
end_date = datetime(2023, 1, 3) # date de fin
# définition de la paire de trading
symbol = 'BTCUSDT'
# Initialisez une liste pour stocker les capitalisations boursières quotidiennes
marketcaps = []

# Parcourez la plage de dates spécifiée
while start_date <= end_date:

    # Formatez la date au format requis pour l'API Binance

    # Récupérez les données de marché pour le Bitcoin sur Binance pour cette journée
    #url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1m&startTime={int(start_date.timestamp()*1000)}&endTime={int(start_date.timestamp()*1000)}'
    #response = requests.get(url)
    response = requests.get('https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=10')
    # conversion des données de réponse JSON en liste de listes
    data = json.loads(response.text)
    print(data)
    # Si des données sont disponibles pour cette journée, calculez la capitalisation boursière pour cette journée
    if response:

        # Extrayez le prix d'ouverture du Bitcoin pour cette journée
        btc_price = float(data[0][4])
        print(btc_price)
        # Extrayez la capitalisation en circulation du Bitcoin pour cette journée
        circulating_supply = float(data[0][8])
        print(circulating_supply)

        # Calculez la capitalisation boursière pour cette journée
        marketcap = btc_price * circulating_supply

        # Ajoutez la capitalisation boursière pour cette journée à la liste
        marketcaps.append((start_date, marketcap))
      
    # Passez à la journée suivante
    start_date += timedelta(days=1)

# Affichez les capitalisations boursières pour chaque jour dans la plage de dates spécifiée
for date, marketcap in marketcaps:
    print('{}: ${:,.2f}'.format(date.strftime('%Y-%m-%d'), marketcap))


"""
import requests
import json
from datetime import datetime, timedelta

# définition de la paire de trading
symbol = 'BTCUSDT'

# définition de l'heure de début (UTC)
start_time = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)

# définition de l'heure de fin (UTC)
end_time = start_time + timedelta(days=1)

# appel de l'API de Binance pour récupérer les données de marché pour la paire de trading spécifiée
url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1m&startTime={int(start_time.timestamp()*1000)}&endTime={int(end_time.timestamp()*1000)}'
response = requests.get(url)

# conversion des données de réponse JSON en liste de listes
data = json.loads(response.text)
print(data)
# boucle à travers les données et affichage des prix de clôture pour chaque minute
for d in data:
    timestamp = datetime.fromtimestamp(d[0]/1000)
    close_price = float(d[4])
    print(f'{timestamp}: {close_price}')
"""

