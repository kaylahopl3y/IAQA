import pandas as pd
import ccxt
import datetime

# Set exchange to FTX (easiest method was to import ccxt)
exchange = ccxt.ftx()

# Define function to get BTC data then print to CSV 
def gather_data_BTC():
    
 # Spot BTC/USD can get API keys to get data that goes further back
 histdatabtc = exchange.fetch_trades('BTC/USD')
 df = pd.DataFrame(histdatabtc)
 df.to_csv('BTChistoricalDataRaw.csv')

 # Perp BTC in ohlcv 5m timeframe
 ohlcvdatabtc = exchange.fetch_ohlcv('BTC-PERP', timeframe='5m')
 df2 = pd.DataFrame(ohlcvdatabtc)
 df2.to_csv('ohlcvData5minRawbtc.csv')
 df2.columns = (['Date Time', 'Open', 'High', 'Low', 'Close', 'Volume'])

 # Convert from ts to date time
 def parse_dates(ts):
  return datetime.datetime.fromtimestamp(ts/1000.0)
 df2['Date Time'] = df2['Date Time'].apply(parse_dates)
 df2.to_csv('BTCohlcvData5min.csv')

# Define function to get ETH data then print to CSV 
def gather_data_ETH():

 # Spot BTC/USD can get API keys to get data that goes further back
 histdataeth = exchange.fetch_trades('ETH/USD')
 df = pd.DataFrame(histdataeth)
 df.to_csv('ETHhistoricalDataRaw.csv')

 # Perp ETH in ohlcv 5m timeframe
 ohlcvdataeth = exchange.fetch_ohlcv('ETH-PERP', timeframe='5m')
 df2 = pd.DataFrame(ohlcvdataeth)
 df2.to_csv('ohlcvData5minRaweth.csv')
 df2.columns = (['Date Time', 'Open', 'High', 'Low', 'Close', 'Volume'])

 # Convert from ts to date time
 def parse_dates(ts):
  return datetime.datetime.fromtimestamp(ts/1000.0)
 df2['Date Time'] = df2['Date Time'].apply(parse_dates)
 df2.to_csv('ETHohlcvData5min.csv')

# Call on functions 
def main():
 gather_data_BTC()
 gather_data_ETH()
if __name__ == '__main__':
 main()
