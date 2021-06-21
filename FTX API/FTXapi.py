import pandas as pd
import requests

markets = requests.get('https://ftx.com/api/markets').json()
df = pd.DataFrame(markets['result'])
df.set_index('name', inplace = True)
df.T

df.to_csv (r'export_dataframe.csv', index = False, header=True)

markets = pd.DataFrame(requests.get('https://ftx.com/api/markets/BTC-0924').json())
markets = markets.drop(['success'], axis=1)
markets.to_csv (r'btcexport_dataframe.csv', index = False, header=True)


