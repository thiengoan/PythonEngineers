import yfinance as yf

stock_symbol = 'AAPL'  # Thay 'AAPL' bằng mã chứng khoán bạn quan tâm
stock_data = yf.download(stock_symbol, start='2022-01-01', end='2023-01-01')

