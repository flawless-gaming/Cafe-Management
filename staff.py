import pandas as pd
import connector
import graph

def staff(): # For an existing staff to login
    while True:
        print('  +----------------------------------+')
        print('  |            Staff Menu            |')
        print('  +----------------------------------+')
        print('  | 1.Login                          |')
        print('  | 2.Register                       |')
        print('  |           ← Back to Main Menu(0) |')
        print('  +----------------------------------+')
        
        df=pd.read_csv('user.csv')
        staff2=dict([(i,a) for i, a in zip(df.user,df.password)])
        key, value = zip(*staff2.items()) # Command used to seperate keys and values of dictionary into a list
        global fu
        fu=int(input('~ Enter Your Choice> '))
        while fu==0 or fu==1 or fu==2:
            if fu==1:
                user=input('> Enter Username> ')
                if user in key:
                    password=input('> Enter Password> ')
                    if password in value:
                        print('~ Log in successful. Welcome '+user+'.')
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
                
            elif fu==2: # To Register a new employee
                h=input("> Owner's username> ")
                pa=input('> Password>')
                if h=='Owner':
                    if pa=='coffeeshop12':
                        print('~ Welcome to Flawless Coffee dear Staff.')
                        print("~ Let's create an account for you.")
                        while True:
                            userid=str(input('> Enter a Username: '))#for a new staff to add user and password 
                            if len(userid)>=5:
                                password=str(input('> Enter a Password: '))
                                # ^ Password should have 8 characters and should not be an obvious one like '1234567890'
                                temp=str(input('> Reenter the Password: '))
                                # ^ This should match with the above entered password
                                if password==temp: # Checking if both the passwords match
                                    if len(password)>=8:
                                        if password not in '1234567890':
                                            df=pd.read_csv('user.csv')
                                            staff2=dict([(i,[a]) for i,a in zip(df.user,df.password)])
                                            staff2.update({userid:password})
                                            # ^ For adding in the new staff and updating data to dictionary
                                            df.loc[len(df.user)]=userid,password
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