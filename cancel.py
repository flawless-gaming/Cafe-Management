import pandas as pd

def remove():
    df=pd.read_csv('order.csv') # Calling order as DataFrame 'df'
    df=df.iloc[:-1,:] # Removing the last row 'Total'
    print('-'*35,df,'-'*35,sep='\n')
    r=int(input('> Enter the index number of the item to be removed> ')) # Taking user input
    # v Creating an if-else condition to check if the input index no. is present in indexes of 'order'
    if r in df.index:
        df=df.drop(r,axis='index') # Removing item data
        df=df.reset_index(drop=True) # To reset the Index
        if len(df.index)==0: # To check whether there are any items left in the order
            x={'Name':['Total'],'Qty':'','Price':[0]}
            df=pd.DataFrame(x)
            print('-'*35,df,'-'*35,sep='\n')
            df=df.to_csv('order.csv',index=False) # To update the .csv file
        else:
            a=len(df.index)
            total=sum(df.Price)
            df.loc[a]='Total',' ',total # To add a new row 'Total'
            print('-'*35,df,'-'*35,sep='\n')
            df=df.to_csv('order.csv',index=False) # To update the .csv file
    else:
        print('!~No Such Product Number Available.')
