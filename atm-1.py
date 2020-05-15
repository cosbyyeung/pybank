# -*- coding: utf-8 -*-
"""
@course: ISOM3400
@author: YEUNG TSZ YAN

"""

import getpass

width = 44
login_tried = 0
endProgram = False


account = {
        "charles":{"password": "thisIsMyPassword",
                   "balance": {"USD": 10,
                                "HKD": 10000,
                               },
                                
                            },
        "samuel":{"password": "secret",
                   "balance": {"USD": 10000,
                                "HKD": 10,
                                "CNY": 50,
                               },
                                
                            },
        }
                   
currency = {
            "USD" : {
                    "USD" : 1,
                    "HKD" : 7.831600,
                    "JPY" : 7.831600/0.074600,
                    "CNY" : 7.831600/1.103100,
                    "EUR" : 7.831600/8.769800,
                    },
            "HKD" : {
                    "USD" : 1/7.862800,
                    "HKD" : 1,
                    "JPY" : 1/0.074600,
                    "CNY" : 1/1.103100,
                    "EUR" : 1/8.769800,
                    },
            "JPY" : {
                    "USD" : 0.073740/7.862800,
                    "HKD" : 0.073740,
                    "JPY" : 1,
                    "CNY" : 0.073740/1.103100,
                    "EUR" : 0.073740/8.769800,
                    },
            "CNY" : {
                    "USD" : 1.088200/7.862800,
                    "HKD" : 1.088200,
                    "JPY" : 1.088200/0.074600,
                    "CNY" : 1,
                    "EUR" : 1.088200/8.769800,
                    },
            "EUR" : {
                    "USD" : 8.640000/7.862800,
                    "HKD" : 8.640000,
                    "JPY" : 8.640000/0.074600,
                    "CNY" : 8.640000/1.103100,
                    "EUR" : 1,
                    },
        }

### Task 2 balance checking function
def check_balance(account, login):
    print("##################################################")
    print("## {} ##".format("".center(width)))
    print("## {} ##".format("Check Balance".center(width)))
    print("## {} ##".format("".center(width)))
    for x in account[login]['balance']:
        width2 = len('##  '+ str(account[login]['balance'][x]))
        print("##  "+ x + " " + str(account[login]['balance'][x]) + "{}##".format("".rjust(44-width2)))
    print("## {} ##".format("".center(width)))
    print("##################################################")
    return False

# Task 3: Cash Withdrawal		  
def cash_withdrawal(account, login):
    ### menu
    print("##################################################")
    print("## {} ##".format("".center(width)))
    print("## {} ##".format("Select your account".center(width)))
    print("## {} ##".format("".center(width)))
    i = 1
    for x in account[login]['balance']:
        width2 = len('##  ' + '. ')
        print("##  " + str(i) + ". " + str(x) + "{}##".format("".rjust(44-width2)))
        i += 1
    print("## {} ##".format("".center(width)))
    print("##################################################")

    ### choose account
    currency_list = list(account.get(login).get('balance').keys())
    account_chosen = int(input("Please choose your account: "))

    while account_chosen > len(currency_list):
        account_chosen = int(input("Invalid input, please enter again: "))
    else:
        max_withdrawal_amount = account.get(login).get('balance').get(currency_list[account_chosen-1])
        withdrawal_amount = input("Please enter withdrawal amount: ")
        while True:
            try:
                withdrawal_amount = int(withdrawal_amount)
                break
            except:
                withdrawal_amount = input("Please enter an integer: ")
        while withdrawal_amount > max_withdrawal_amount or withdrawal_amount > 50000:
            if withdrawal_amount > max_withdrawal_amount:
                withdrawal_amount = input("The withdrawal amount you entered exceeded your account balance, please try again: ")
                while True:
                    try:
                        withdrawal_amount = int(withdrawal_amount)
                        break
                    except:
                        withdrawal_amount = input("Please enter an integer: ")
            else:
                withdrawal_amount = input("The withdrawal amount you entered exceeded the $50000 withdrawal limit, please try again: ")
                while True:
                    try:
                        withdrawal_amount = int(withdrawal_amount)
                        break
                    except:
                        withdrawal_amount = input("Please enter an integer: ")
        else:
            account[login]['balance'][currency_list[account_chosen-1]] = account[login]['balance'][currency_list[account_chosen-1]] - withdrawal_amount
            print("##################################################")
            print("## {} ##".format("".center(width)))
            print("## {} ##".format("Withdrawal Accepted!".center(width)))
            print("## {} ##".format("".center(width)))
            print("##  1. Check Balance" + "{}##".format("".rjust(28)))
            print("##  2. Exit" + "{}##".format("".rjust(37)))
            print("## {} ##".format("".center(width)))
            print("##################################################")

            option = int(input("Enter the option: "))
            while True:
                if option == 1:
                    check_balance(account, login)
                    break
                elif option == 2:
                    return True
                else:
                    option = int(input("Invalid input, please enter the option again: "))
    return False

# Task 4: Transfer money to other user
def transfer(account, login):
    



    return False
                
	


# Task 5: Currency Exchange
def currency_exchange(account, login):

                
				
				
    return False
    
   

# welcome page

print("##################################################")
print("## {} ##".format("".center(width)))
print("## {} ##".format("Welcome to PyBank".center(width)))
print("## {} ##".format("".center(width)))
print("##################################################")
      
# Task 1: login validation
login = input("Login Name: ")
while login not in account:
    login = input("Invalid login name, please enter your login name again: ")
else:
    password_entered = input("Please enter your password, "+str(3-login_tried)+" attempts remaining: ")
    login_tried += 1
    while True:
        if password_entered != account[login]['password'] and login_tried <= 2:
            password_entered = input("Invalid password, please enter again, "+str(3-login_tried)+" attempts remaining: ")
            login_tried += 1
        elif password_entered == account[login]['password']:
            print("Login successful")
            break
        else:
            print('Login unsuccessful')
            endProgram = True
            break


####### Task 1 end

while not endProgram:
    # menu page
    menuoption = ""

    while not menuoption in ["1", "2", "3", "4","5"]: 
        
        print("##################################################")
        print("## {} ##".format("".center(width)))
        print("## {} ##".format("Please select service".center(width)))
        print("## {} ##".format("".center(width)))
        print("## {} ##".format("1. Cash Withdrawal ".ljust(width)))
        print("## {} ##".format("2. Transfer".ljust(width)))
        print("## {} ##".format("3. Account Balance".ljust(width)))
        print("## {} ##".format("4. Currency Exchange".ljust(width)))
        print("## {} ##".format("5. Exit".ljust(width)))
        print("## {} ##".format("".center(width)))
        print("## {} ##".format("#"*width))
        menuoption = input("Enter the option: ")

    else:
        if menuoption == "1":
            endProgram = cash_withdrawal(account, login)
            input("Press Enter to continue...")
            
        elif menuoption == "2":
            endProgram = transfer(account, login)
            input("Press Enter to continue...")
            
        elif menuoption == "3":
            endProgram = check_balance(account, login)
            input("Press Enter to continue...")
            
        elif menuoption == "4":
            endProgram = currency_exchange(account, login)
            input("Press Enter to continue...")
            
        elif menuoption == "5":
            endProgram = True

print("Bye!")
input("Press Enter to end the program...")
