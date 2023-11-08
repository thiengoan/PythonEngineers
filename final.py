from flask import Flask
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world"

@app.route("/download_stock")
def download_stock():
    stock_symbol = 'AAPL' 
    stock_data = yf.download(stock_symbol, start='2022-01-01', end='2022-12-31')
    return stock_data.to_csv("final.csv")

@app.route("/show_chart")    
def get_stock():
    df = pd.read_csv('final.csv')
    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
    fig.show()

@app.route("/chart_bollinger")    
def chart_bollinger():
    df = pd.read_csv('final.csv')
    df = bollinger_bands(df, 20, 2)

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df['Date'], y=df['Adj Close'] , mode='lines', name='Adj Close'))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['BU'], mode='lines', name='BU', line=dict(color='firebrick', width=1, dash='dash')))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['BL'], mode='lines', name='BL', line=dict(color='royalblue', width=1, dash='dash')))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['BU'], fill='tonexty', fillcolor='rgba(0,100,80,0.2)', line_color='rgba(255,255,255,0)', showlegend=False))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['B_MA'],mode='lines',name='B_MA'))

    fig.show()
    
def inc_dec(c, o):  #param ( c: Close , o: Open )
    if c > o:
        value="Increase"
    elif c < o:
        value="Decrease"
    else:
        value="Equal"
    return value

def bollinger_bands(df, n, m):
    # n = smoothing length
    # m = number of standard deviations away from MA
    
    #typical price
    TP = (df['High'] + df['Low'] + df['Close']) / 3
    # but we will use Adj close instead for now, depends
    data = TP
    #data = df['Adj Close']

    # takes one column from dataframe
    B_MA = pd.Series((data.rolling(n, min_periods=n).mean()), name='B_MA')
    sigma = data.rolling(n, min_periods=n).std() 
    BU = pd.Series((B_MA + m * sigma), name='BU')
    BL = pd.Series((B_MA - m * sigma), name='BL')
    
    df = df.join(B_MA)
    df = df.join(BU)
    df = df.join(BL)

    return df

if __name__ == "__main__":
    app.run()

