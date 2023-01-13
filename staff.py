import pandas as pd
import connector
import graph

#making a staff member login or adding a new staff member
def staff():
    while True:
        print('  +----------------------------------+')
        print('  |            Staff Menu            |')
        print('  +----------------------------------+')
        print('  | 1.Login                          |')
        print('  | 2.Register                       |')
        print('  |           ← Back to Main Menu(0) |')
        print('  +----------------------------------+')
        HOST='host'#a single host to add a new staff
        passw='hpassw'#host password
        df=pd.read_csv('user.csv')
        staff2=dict([(i,a) for i, a in zip(df.user,df.password)])
        key, value = zip(*staff2.items())#command used to sepperate keys and value from dictionary to list
        global fu
        fu=int(input('~ Enter Your Choice> '))
        while fu==1 or fu==2 or fu==0:
            if fu==1:#fu is used to enter the first part of the loop
                user=input('> Enter Username: ')
                if user in key:#user from staff is used 
                    password=input('> Enter Password: ')#enter password of staff
                    if password in value:
                        print('~ Log in successful. Welcome '+user+'.')#prints 'loged in' when when a staffs username and password is correct
                        while True:
                            print('  +----------------------------------+')
                            print('==|            Staff Menu            |')
                            print('  +----------------------------------+')
                            print('  | 1.Show Data                      |')
                            print('  | 2.Verify Data                    |')
                            print('  | 3.Sales Analysis(Product-wise)   |')
                            print('  | 4.Daily Sales Analysis           |')
                            print('  |           ← Back to Main Menu(0) |')
                            print('  +----------------------------------+')
                            b=int(input('~ Enter Your Choice> '))
                            if b==1:
                                connector.show()
                                mm=input('~ Press Enter to go to Main Menu ')
                            if b==2:
                                connector.verify()
                                mm=input('~ Press Enter to go to Main Menu ')
                            if b==3:
                                graph.product_sales()
                                mm=input('~ Press Enter to go to Main Menu ')
                            if b==4:
                                graph.daily_sales()
                                mm=input('~ Press Enter to go to Main Menu ')
                            if b==0:
                                print()
                                staff()
                    else:
                        print('!~ Incorrect Password. Please try again.')
                        continue
                else:
                    print('!~ This page can only be accessed by the staff.')
                    print('~ If you are a new joinee, register with the help of the owner to continue.')
                    break
                    #this is the second part of the loop
                    #this part for the host to enter and add a staff member
                
            elif fu==2: 
                h=input("> Owner's username:")
                pa=input('> Password:')
                if h==HOST:
                    if pa==passw:
                        print('~ Welcome to Flawless Coffee dear Staff.')
                        print("~ Let's create an account for you.")
                        while True:
                            userid=str(input('> Enter a Username: '))#for a new staff to add user and password 
                            if len(userid)>=5:
                                password=str(input('> Enter a Password: '))
                                temp=str(input('> Reenter the Password: '))
                                if password==temp:    
                                    if len(password)>=8:
                                        if password not in '1234567890':
                                            df=pd.read_csv('user.csv')
                                            staff2=dict([(i,[a]) for i,a in zip(df.user,df.password)])
                                            staff2.update({userid:password})#for adding in the new staff and updating data to dictionary
                                            df.loc[len(df.user)]=userid,password
                                            print(staff2)#only to check wether the data is updated or not
                                            df=df.to_csv('user.csv',index=False)
                                            staff()
                                        else:
                                            print('!~ Please enter a less obvious password.')
                                            continue
                                    else:
                                        print('!~ Password is too short. Enter atleast 8 characters.')
                                        continue
                                else:
                                    print("!~ Entered Passwords don't match. Please try again.")
                                    continue
                            else:
                                print('!~ Username is too short. Enter atleast 5 characters.')
                                continue
                    else:
                        print('!~ Incorrect Password. Please try again.')
                        continue
                else:
                    print('!~ This page can only be accessed by the owner.')
                    break
            
            elif fu==0:
                import main
                main.startmenu()
        #loop ends at this part and starts from a begin of the first loop