Stock Market Analyzer - Google (GOOGL)

Overview

This Python-based Stock Market Analyzer is designed to fetch, clean, analyze, and visualize historical stock price data for Google (GOOGL) using yfinance. The project provides tools for candlestick charting, moving averages, and monthly resampling, helping traders and investors gain insights into trends and correlations.

Features

✅ Historical Data Retrieval: Fetch Google stock data from Yahoo Finance

✅ Data Cleaning & Processing: Ensures numerical accuracy and removes invalid rows

✅ Moving Averages (MA & EMA): Computes 20-day & 50-day averages for trend analysis

✅ Monthly Resampling: Aggregates daily closing prices into monthly averages

✅ Candlestick Visualization: Uses mplfinance for professional stock charting

✅ Automatic Handling of Large Data: Switches between candlestick and line charts when dataset is too large

Installation
- Clone the repository:
git clone https://github.com/your-username/stock-market-analyzer.git
cd stock-market-analyzer

- Install dependencies:
pip install pandas yfinance matplotlib seaborn mplfinance


Usage
Run the script to fetch and analyze Google stock data:
python stock_market_analyser.py


This will:
- Download historical data and save it as a CSV
- Compute moving averages
- Plot Google’s candlestick chart
- Display monthly resampled data
Example Output
- Monthly Average Stock Prices:
Date      
2020-01-31    1350.54  
2020-02-29    1382.76  
2020-03-31    1114.22  
- 
- Candlestick Chart with Moving Averages

License

This project is licensed under the MIT License.

Contributions

Feel free to fork, improve, and open issues!
