import pandas as pd

def orders():
    print(' +----------------------------------+')
    print(' |            Your Order            |')
    print(' +----------------------------------+')
    df=pd.read_csv('order.csv')
    print(df)
    # ^ Calling and printing Bill as DataFrame 'df'