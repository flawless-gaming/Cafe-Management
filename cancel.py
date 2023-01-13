import pandas as pd
#function remove is created
def remove():
    df=pd.read_csv('order.csv')
    df=df.iloc[:-1,:]
    print(df)
    r=int(input("Enter the Product to Remove="))
    if r in df.index:
        df=df.drop(r,axis='index')
        df = df.reset_index(drop=True)
        if len(df.index)==0:
            x={'Name':['TOTAL'],
               'QTY':'',
               'Price':[0]}
            df=pd.DataFrame(x)
            print(df)
            df=df.to_csv('order.csv',index=False)
        else:
            a=len(df.index)
            total=sum(df.Price)
            df.at[a]='TOTAL',' ',total
            print(df)
            df=df.to_csv('order.csv',index=False)
    else:
        print('No Such Product Number Available')