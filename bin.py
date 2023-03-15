import requests
from datetime import datetime, timedelta
import json


symbol = 'BTCUSDT'
# Initialisez une liste pour stocker les capitalisations boursières quotidiennes
marketcaps = []

# Récupérez les données de marché pour le Bitcoin sur Binance pour cette journée
response = requests.get('https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=10')

# conversion des données de réponse JSON en liste de listes
data = json.loads(response.text)
print(data)
print(len(data))

# Si des données sont disponibles pour cette journée, calculez la capitalisation boursière pour cette journée
if response:
    for i in range(len(data)):
        # Extrayez le prix de cloture du Bitcoin pour cette journée
        btc_price = float(data[i][4])
        print(btc_price)
        # Extrayez la capitalisation en circulation du Bitcoin pour cette journée
        circulating_supply = float(data[i][10])
        print(circulating_supply)

        # Calculez la capitalisation boursière pour cette journée
        marketcap = btc_price * circulating_supply

        # Ajoutez la capitalisation boursière pour cette journée à la liste
        marketcaps.append(marketcap)
        
# Affichez les capitalisations boursières pour chaque jour dans la plage de dates spécifiée
for marketcap in marketcaps:
    print('${:,.2f}'.format(marketcap))




import requests
import json

# Set the API endpoint URL
url = 'https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT'


# Send a GET request to the endpoint and retrieve the response
response = requests.get(url)

# Parse the response JSON data
data = json.loads(response.text)

print(data)
# Extract the historical circulating supply data
circulating_supply = data['count']

# Print the circulating supply data
print(f"Historical circulating supply of Bitcoin: {circulating_supply}")




import requests

# Set the API endpoint and parameters
endpoint = "https://api.binance.com/api/v3/klines"
symbol = "BTCUSDT"
interval = "1d"
start_time = "1640995200000"  # Unix timestamp for 2022-01-01 00:00:00 UTC
end_time = "1641081599999"  # Unix timestamp for 2022-01-01 23:59:59 UTC

# Make the API call
params = {"symbol": symbol, "interval": interval, "startTime": start_time, "endTime": end_time}
response = requests.get(endpoint, params=params)
data = response.json()

# Extract the closing price and total volume for each day
closing_prices = [float(entry[4]) for entry in data]
total_volumes = [float(entry[7]) for entry in data]
print(len(data))
# Calculate the market capitalization for each day
market_caps = [closing_prices[i] * (total_volumes[i] / len(data)) for i in range(len(data))]

print(f"The historical market capitalization of {symbol} on 2022-01-01 was ${market_caps[-1]:.2f}.")







import requests



import requests
import json


import requests
import json

from datetime import datetime

start_time_ms = 1675507200000
end_time_ms = 1675593599999



# Set the API endpoint and parameters
url = "https://api.binance.com/api/v3/klines"
params = {
    "symbol": "BTCUSDT",
    "interval": "1d",
    "startTime": str(start_time_ms), # Start time in milliseconds since Unix epoch (02/03/2023)
    "endTime": str(end_time_ms) # End time in milliseconds since Unix epoch (02/03/2023)
}

# Make a request to the Binance API to get the klines data
response = requests.get(url, params=params)

# Parse the JSON response to get the market cap
klines = json.loads(response.text)

print(klines)
market_cap = float(klines[-1][4]) * float(klines[-1][5])

# Print the market cap
print(f"The market cap of Bitcoin on 02/03/2023 was ${market_cap:.2f}")
