import yfinance as yf
import pandas as pd

def get_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end)
    return data

df = get_data("AAPL", "2020-01-01", "2025-01-01") #YMD
print(df.head(10))
#df.to_csv("APPL_data.csv")

def add_signal(df):
    df["SMA_50"] = df["Close"].rolling(window=50).mean()
    df["SMA_20"] = df["Close"].rolling(window=20).mean()
    return df

df = add_signal(df)
print(df[["Close", "SMA_50", "SMA_20"]].head(60))
