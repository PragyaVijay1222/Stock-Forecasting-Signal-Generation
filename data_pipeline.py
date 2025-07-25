import yfinance as yf
import pandas as pd
import ta

def download_data(ticker='AAPL', start='2020-01-01', end='2024-12-31'):
    df = yf.download(ticker, start=start, end=end)
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    df.dropna(inplace=True)
    return df

def add_technical_indicators(df):
    close_series = df['Close'].squeeze()
    df['RSI'] = ta.momentum.RSIIndicator(close_series).rsi()
    df['MACD'] = ta.trend.MACD(close_series).macd()
    bb = ta.volatility.BollingerBands(close_series)
    df['Bollinger_High'] = bb.bollinger_hband()
    df['Bollinger_Low'] = bb.bollinger_lband()
    df.dropna(inplace=True)
    return df

def save_data(df, filename='processed_data.csv'):
    df = df.copy()
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'Date'}, inplace=True)
    df.to_csv(filename, index=False)
    print(f"✅ Data saved to {filename}")

if __name__ == "__main__":
    df = download_data('AAPL')
    df = add_technical_indicators(df)
    save_data(df)
