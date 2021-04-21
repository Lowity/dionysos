import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.cryptocurrencies import CryptoCurrencies
import matplotlib.pyplot as plt
from coinmarketcap import Market

#key = "ECTDBRGFM8H7H2MR"
key = "OQ8414OJXCDP4DCV"

def get_gme():
    ts = TimeSeries(key, output_format="pandas")
    data_gme, meta = ts.get_daily("GME", outputsize="compact")

    data_gme = data_gme.reset_index()
    data_gme_x = data_gme.drop(["1. open", "2. high", "3. low", "4. close", "5. volume"], axis=1)
    data_gme_x = pd.to_datetime(data_gme_x["date"].unique()).tolist()

    data_gme_y = data_gme.drop(["date", "1. open", "2. high", "3. low", "5. volume"], axis=1)
    data_gme_y = data_gme_y["4. close"].values.tolist()

    return data_gme_x, data_gme_y


def get_bitcoin():
    cc = CryptoCurrencies(key='YOUR_API_KEY', output_format='pandas')
    data_btc, meta_data = cc.get_digital_currency_daily(symbol='BTC', market='CNY')
    data_btc = data_btc.reset_index()
    data_btc = data_btc.drop(data_btc.index[100:1000], 0)
    data_btc_x = data_btc.drop(labels=["1a. open (CNY)", "1b. open (USD)", "2a. high (CNY)", "2b. high (USD)", "3a. low (CNY)", "3b. low (USD)", "4a. close (CNY)", "4b. close (USD)", "5. volume", "6. market cap (USD)"], axis=1)
    data_btc_x = pd.to_datetime(data_btc_x["date"].unique()).tolist()

    data_btc_y = data_btc.drop(labels=["date", "1a. open (CNY)", "1b. open (USD)", "2a. high (CNY)", "2b. high (USD)", "3a. low (CNY)", "3b. low (USD)", "4a. close (CNY)", "5. volume", "6. market cap (USD)"], axis=1)
    data_btc_y = data_btc_y.rename(columns={"4b. close (USD)": "Close"})
    data_btc_y = data_btc_y["Close"].values.tolist()

    return data_btc_x, data_btc_y


