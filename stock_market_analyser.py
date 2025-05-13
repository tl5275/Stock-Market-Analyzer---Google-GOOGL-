import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import mplfinance as mpf

# 1. Download data and save as CSV
def get_stock_data(ticker, start="2020-01-01", end="2024-12-31"):
    df = yf.download(ticker, start=start, end=end, auto_adjust=False)  # Explicitly setting auto_adjust
    df.reset_index(inplace=True)  # Ensure 'Date' is a column
    df.to_csv(f"{ticker}.csv", index=False)

# 2. Load CSV safely and clean
def load_csv(ticker):
    df = pd.read_csv(f"{ticker}.csv", parse_dates=['Date'])
    df.set_index('Date', inplace=True)
    for col in ['Open', 'High', 'Low', 'Close', 'Volume']:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df.dropna(subset=['Open', 'High', 'Low', 'Close', 'Volume'], inplace=True)
    return df

# 3. Add moving averages
def add_moving_averages(df, windows=[20, 50], ewma=True):
    for window in windows:
        df[f"MA_{window}"] = df['Close'].rolling(window).mean()
        if ewma:
            df[f"EMA_{window}"] = df['Close'].ewm(span=window, adjust=False).mean()
    return df

# 4. Resample to monthly
def resample_monthly(df):
    return df['Close'].resample('ME').mean()

# 5. Candlestick plotting with large dataset handling
def plot_candlestick(df, title="Stock Chart"):
    if len(df) > 1000:  # Adjust threshold for large datasets
        print("Too much data to display clear candlesticks. Using 'line' plot instead.")
        mpf.plot(df, type='line', volume=True, title=title, style='yahoo')
    else:
        mpf.plot(df, type='candle', mav=(20, 50), volume=True, title=title, style='yahoo', warn_too_much_data=1000)

# === Main Execution ===
if __name__ == "__main__":
    ticker = 'GOOGL'  # Only Google stock

    # Step 1: Download and save
    get_stock_data(ticker)

    # Step 2: Load and process the ticker
    print(f"\nProcessing {ticker}...")
    df = load_csv(ticker)
    df = add_moving_averages(df)

    # Monthly average print
    monthly_avg = resample_monthly(df)
    print(f"\n--- {ticker} Monthly Averages ---")
    print(monthly_avg.head())

    # Candlestick chart
    plot_candlestick(df, title=f"{ticker} Candlestick with MAs")