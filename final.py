from flask import Flask
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go

app = Flask(__name__)

@app.route("/")
def hello_world():
    df = pd.read_csv('final.csv')
    #df = bollinger_bands(df, 20, 2)

    agg_dict = {'Open': 'first',
            'High': 'max',
            'Low': 'min',
            'Close': 'last',
            'Adj Close': 'last',
            'Volume': 'mean'}

    # resampled dataframe
    # 'W' means weekly aggregation
    #df.set_index(['Date'], inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index(['Date'], inplace=True)
    df_agg = df.resample('W').agg(agg_dict)
    #df_agg = df.agg(agg_dict)
    df_agg = df_agg.reset_index()
    print(df_agg)
    # return "Hello world"

@app.route("/download_stock")
def download_stock():
    stock = 'BIDU' 
    stock_data = yf.download(stock, start='2017-01-01', end='2020-07-30')
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
    fig.add_trace(go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close']))
    # fig.add_trace(go.Scatter(x=df['Date'], y=df['Adj Close'] , mode='lines', name='Adj Close'))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['BU'], mode='lines', name='BU', line=dict(color='firebrick', width=1, dash='dash')))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['BL'], mode='lines', name='BL', line=dict(color='royalblue', width=1, dash='dash')))
    #fig.add_trace(go.Scatter(x=df['Date'], y=df['BU'], fill='tonexty', fillcolor='rgba(0,100,80,0.2)', line_color='rgba(255,255,255,0)', showlegend=False))
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

'''
Công thức tính Bollinger bands
- Dải giữa là đường trung bình động chu kỳ 20 ngày (SMA20), được tính bằng giá trị trung bình của giá đóng cửa.
- Dải trên = SMA20 ngày + 2 x Độ lệch chuẩn 20 ngày.
- Dải dưới = SMA20 ngày – 2 x Độ lệch chuẩn 20 ngày.

*** 

Khi giá cổ phiếu bằng hoặc cao hơn dải trên, cổ phiếu có thể bị mua quá mức.
Khi giá cổ phiếu bằng hoặc thấp hơn biên độ, cổ phiếu có thể bị bán quá mức.

'''
def bollinger_bands(df, n, m):
    TP = (df['High'] + df['Low'] + df['Close']) / 3
    data = TP
    B_MA = pd.Series((data.rolling(n, min_periods=n).mean()), name='B_MA')
    sigma = data.rolling(n, min_periods=n).std() 
    BU = pd.Series((B_MA + m * sigma), name='BU')
    BL = pd.Series((B_MA - m * sigma), name='BL')
    df = df.join(B_MA)
    df = df.join(BU)
    df = df.join(BL)
    return df

@app.route("/chart_bollinger_weekly")    
def chart_bollinger_weekly():
    df = pd.read_csv('final.csv')
    #df = bollinger_bands(df, 20, 2)
    #df = bollinger_bands(df, 20, 2)

    agg_dict = {'Open': 'first',
            'High': 'max',
            'Low': 'min',
            'Close': 'last',
            'Adj Close': 'last',
            'Volume': 'mean'}

    # resampled dataframe
    # 'W' means weekly aggregation
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df_agg = df.resample('W').agg(agg_dict)
    df_agg = df_agg.reset_index()

    df_agg = bollinger_bands(df_agg, 20, 2)
    df_agg = add_signal(df_agg)

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df_agg['Date'], y=df_agg['Adj Close'] , mode='lines', name='Adj Close'))
    fig.add_trace(go.Scatter(x=df_agg['Date'], y=df_agg['High'] , mode='lines', name='High'))
    fig.add_trace(go.Scatter(x=df_agg['Date'], y=df_agg['Close'] , mode='lines', name='Close'))
    fig.add_trace(go.Scatter(x=df_agg['Date'], y=df_agg['BU'], mode='lines', name='BU', line=dict(color='firebrick', width=1, dash='dash')))
    fig.add_trace(go.Scatter(x=df_agg['Date'], y=df_agg['BL'], mode='lines', name='BL', line=dict(color='royalblue', width=1, dash='dash')))
    #fig.add_trace(go.Scatter(x=df['Date'], y=df['BU'], fill='tonexty', fillcolor='rgba(0,100,80,0.2)', line_color='rgba(255,255,255,0)', showlegend=False))
    #fig.add_trace(go.Scatter(x=df['Date'], y=df['B_MA'],mode='lines',name='B_MA'))
    fig.add_trace(go.Scatter(x=df_agg['Date'], y=df_agg['Buy'] , mode='markers', name='Buy',marker=dict(
                symbol="arrow-up",
                size=15
            ),))
    fig.add_trace(go.Scatter(x=df_agg['Date'], y=df_agg['Sell'] , mode='markers', name='Sell',
                             marker=dict(
                symbol="arrow-down",
                size=15
            ),))
    fig.show()

def add_signal(df):
    # adds two columns to dataframe with buy and sell signals
    buy_list = []
    sell_list = []
    
    for i in range(len(df['Close'])):
        #if df['Close'][i] > df['BU'][i]:           # sell signal     daily
        if df['High'][i] > df['BU'][i]:             # sell signal     weekly
            buy_list.append(np.nan)
            sell_list.append(df['Close'][i])
        #elif df['Close'][i] < df['BL'][i]:         # buy signal      daily
        elif df['Low'][i] < df['BL'][i]:            # buy signal      weekly
            buy_list.append(df['Close'][i])
            sell_list.append(np.nan)  
        else:
            buy_list.append(np.nan)
            sell_list.append(np.nan)
         
    buy_list = pd.Series(buy_list, name='Buy')
    sell_list = pd.Series(sell_list, name='Sell')
        
    df = df.join(buy_list)
    df = df.join(sell_list)        
     
    return df

if __name__ == "__main__":
    app.run()

