import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test():
    df = pd.read_csv('final.csv')
    plt.figure()
    plt.plot(df['Date'], df['Low'])
    plt.title('Price chart (Adj Close)')
    plt.show()

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

test()