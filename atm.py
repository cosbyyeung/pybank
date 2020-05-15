# -*- coding: utf-8 -*-

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
    ### Check Balance window
    print("##################################################")
    print("## {} ##".format("".center(width)))
    print("## {} ##".format("Check Balance".center(width)))
    print("## {} ##".format("".center(width)))

    ### display all account and their balance
    for x in account[login]['balance']:
        width2 = len('##  '+ str(account[login]['balance'][x]))
        print("##  "+ x + " " + str(account[login]['balance'][x]) + "{}##".format("".rjust(44-width2)))

    print("## {} ##".format("".center(width)))
    print("##################################################")
    return False

# Task 3: Cash Withdrawal

def cash_withdrawal(account, login):
    ### Account selection window
    print("##################################################")
    print("## {} ##".format("".center(width)))
    print("## {} ##".format("Select your account".center(width)))
    print("## {} ##".format("".center(width)))

    ### display all account
    i = 1
    for x in account[login]['balance']:
        width2 = len('##  ' + '. ')
        print("##  " + str(i) + ". " + str(x) + "{}##".format("".rjust(44-width2)))
        i += 1

    print("## {} ##".format("".center(width)))
    print("##################################################")

    ### get user account
    currency_list = list(account.get(login).get('balance').keys())
    account_chosen = int(input("Please choose your account: "))

    ### validate user input
    while account_chosen > len(currency_list):
        account_chosen = int(input("Invalid input, please enter again: "))
    else:
        ### get user account balance
        max_withdrawal_amount = account.get(login).get('balance').get(currency_list[account_chosen-1])
        withdrawal_amount = input("Please enter withdrawal amount: ")
        while True:
            ### validate if user input is integer
            try:
                withdrawal_amount = int(withdrawal_amount)
                break
            except:
                withdrawal_amount = input("Please enter an integer: ")

        ### check if withdrawal amount exceed account balance or $50000
        while withdrawal_amount > max_withdrawal_amount or withdrawal_amount > 50000:
            if withdrawal_amount > max_withdrawal_amount:
                ### display prompt when withdrawal amount exceed account balance
                withdrawal_amount = input("The withdrawal amount you entered exceeded your account balance, please try again: ")
                while True:
                    try:
                        withdrawal_amount = int(withdrawal_amount)
                        break
                    except:
                        withdrawal_amount = input("Please enter an integer: ")
            else:
                ### display prompt when withdrawal amount exceed $50000
                withdrawal_amount = input("The withdrawal amount you entered exceeded the $50000 withdrawal limit, please try again: ")
                while True:
                    try:
                        withdrawal_amount = int(withdrawal_amount)
                        break
                    except:
                        withdrawal_amount = input("Please enter an integer: ")
        else:
            ### update account balance
            account[login]['balance'][currency_list[account_chosen-1]] = account[login]['balance'][currency_list[account_chosen-1]] - withdrawal_amount

            ### Selection window for successful withdrawal
            print("##################################################")
            print("## {} ##".format("".center(width)))
            print("## {} ##".format("Withdrawal Accepted!".center(width)))
            print("## {} ##".format("".center(width)))
            print("##  1. Check Balance" + "{}##".format("".rjust(28)))
            print("##  2. Exit" + "{}##".format("".rjust(37)))
            print("## {} ##".format("".center(width)))
            print("##################################################")

            ### get user input to check balance after withdrawal or exit the program
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

    ### Account selection window
    print("##################################################")
    print("## {} ##".format("".center(width)))
    print("## {} ##".format("Select your account".center(width)))
    print("## {} ##".format("".center(width)))

    ### display user accounts
    i = 1
    for x in account[login]['balance']:
        width2 = len('##  ' + '. ')
        print("##  " + str(i) + ". " + str(x) + "{}##".format("".rjust(44 - width2)))
        i += 1

    print("## {} ##".format("".center(width)))
    print("##################################################")

    ### get user account
    currency_list = list(account.get(login).get('balance').keys())
    account_chosen = int(input("Please choose your account: "))

    ### validate user input
    while account_chosen > len(currency_list):
        account_chosen = int(input("Invalid input, please enter again: "))
    else:
        ### get user input for amount of money to transfer
        receiver_account = input("Please enter the receiver's account: ")
        ### check if the receiver's account exist
        while receiver_account not in account:
            receiver_account = input("Invalid receiver's account, please enter again: ")
        else:
            ### check if receiver has the currency account
            receiver_currency_list = list(account.get(receiver_account).get('balance').keys())
            if currency_list[account_chosen - 1] in receiver_currency_list:
                transfer_amount = input("Please enter transfer amount: ")
                ### check if user input is integer
                while True:
                    try:
                        transfer_amount = int(transfer_amount)
                        break
                    except:
                        transfer_amount = input("Please enter an integer: ")
                ### check sender's account balance
                max_transfer_amount = account.get(login).get('balance').get(currency_list[account_chosen - 1])
                ### check if transfer amount exceeds account balance or $10000
                while transfer_amount > max_transfer_amount or transfer_amount > 10000:
                    if transfer_amount > max_transfer_amount:
                        ### display prompt when transfer amount exceed user's account balance
                        transfer_amount = input(
                            "The transfer amount you entered exceeded your account balance, please try again: ")
                        while True:
                            try:
                                transfer_amount = int(transfer_amount)
                                break
                            except:
                                transfer_amount = input("Please enter an integer: ")
                    else:
                        ### display prompt when transfer amount exceed withdrawal limit
                        transfer_amount = input(
                            "The transfer amount you entered exceeded the $10000 withdrawal limit, please try again: ")
                        while True:
                            try:
                                transfer_amount = int(transfer_amount)
                                break
                            except:
                                transfer_amount = input("Please enter an integer: ")
                else:
                    ### update account balance for sender
                    account[login]['balance'][currency_list[account_chosen - 1]] \
                        = account[login]['balance'][currency_list[account_chosen - 1]] - transfer_amount
                    ### update account balance for receiver
                    account[receiver_account]['balance'][currency_list[account_chosen - 1]] \
                        = account[receiver_account]['balance'][currency_list[account_chosen - 1]] + transfer_amount
                    ### Transfer successful window
                    print("##################################################")
                    print("## {} ##".format("".center(width)))
                    print("## {} ##".format("Transfer Accepted!".center(width)))
                    print("## {} ##".format("".center(width)))
                    print("##  1. Check Balance" + "{}##".format("".rjust(28)))
                    print("##  2. Exit" + "{}##".format("".rjust(37)))
                    print("## {} ##".format("".center(width)))
                    print("##################################################")

                    ### get user input for action - Check Balance/ Exit
                    option = int(input("Enter the option: "))
                    while True:
                        if option == 1:
                            check_balance(account, login)
                            break
                        elif option == 2:
                            return True
                        else:
                            option = int(input("Invalid input, please enter the option again: "))
            else:
                ### exit to home menu if the receiver does not have the currency account
                print("The receiver does not have the currency account you chose, exiting to home menu..")
                return False


# Task 5: Currency Exchange
def currency_exchange(account, login):
    ### Account selection window
    print("##################################################")
    print("## {} ##".format("".center(width)))
    print("## {} ##".format("Select your account".center(width)))
    print("## {} ##".format("".center(width)))

    ### display accounts
    i = 1
    for x in account[login]['balance']:
        width2 = len('##  ' + '. ')
        print("##  " + str(i) + ". " + str(x) + "{}##".format("".rjust(44 - width2)))
        i += 1

    print("## {} ##".format("".center(width)))
    print("##################################################")

    ### get user account to exchange money from
    currency_list = list(account.get(login).get('balance').keys())
    account_chosen = int(input("Please choose your account to exchange from: "))

    ### validate user input
    while account_chosen > len(currency_list):
        account_chosen = int(input("Invalid input, please enter again: "))
    else:
        ### Selection window for currency to exchange to
        print("##################################################")
        print("## {} ##".format("".center(width)))
        print("## {} ##".format("Select a currency to exchange to".center(width)))
        print("## {} ##".format("".center(width)))

        ### display currency option
        i = 1
        for x in currency:
            width2 = len('##  ' + '. ')
            print("##  " + str(i) + ". " + str(x) + "{}##".format("".rjust(44 - width2)))
            i += 1

        print("## {} ##".format("".center(width)))
        print("##################################################")

        ### get user input for currency to exchange to
        account_chosen_2 = int(input("Please select the currency: "))
        while True:
            ### validate user input
            if account_chosen_2 in range(1,6):
                currency_list_2 = list(currency.keys())
                ### create variable FROM_currency and TO_currency
                FROM_currency = currency_list[account_chosen - 1]
                TO_currency = currency_list_2[account_chosen_2 - 1]
                ### create new currency account if user does not already have the currency account
                if TO_currency not in account[login]['balance']:
                    account[login]['balance'][TO_currency] = 0
                else:
                    ### get user input for exchange amount in currency to be exchanged to
                    exchange_amount_TO_currency = input("Please enter exchange amount in "+TO_currency+": ")
                    while True:
                        ### validate user input
                        try:
                            exchange_amount_TO_currency = int(exchange_amount_TO_currency)
                            break
                        except:
                            exchange_amount_TO_currency = input("The exchange amount you entered is not an integer, please enter again: ")
                    ### check account balance
                    max_exchange_amount = account.get(login).get('balance').get(FROM_currency) / currency[TO_currency][FROM_currency]
                    ### check if exchange amount exceed account balance
                    while exchange_amount_TO_currency > max_exchange_amount:
                        exchange_amount_TO_currency = input("The exchange amount you entered exceeded your account balance, please try again: ")
                        ### validate user input
                        while True:
                            try:
                                exchange_amount_TO_currency = int(exchange_amount_TO_currency)
                                break
                            except:
                                exchange_amount_TO_currency = input("Please enter an integer: ")
                    else:
                        ### update both accounts' balance
                        exchange_amount_FROM_currency = exchange_amount_TO_currency * currency[TO_currency][FROM_currency]
                        account[login]['balance'][FROM_currency] = account[login]['balance'][FROM_currency] - exchange_amount_FROM_currency
                        account[login]['balance'][TO_currency] = account[login]['balance'][TO_currency] + exchange_amount_TO_currency

                        ### Selection window for successful exchange
                        print("##################################################")
                        print("## {} ##".format("".center(width)))
                        print("## {} ##".format("Exchange Successful!".center(width)))
                        print("## {} ##".format("".center(width)))
                        print("##  1. Check Balance" + "{}##".format("".rjust(28)))
                        print("##  2. Exit" + "{}##".format("".rjust(37)))
                        print("## {} ##".format("".center(width)))
                        print("##################################################")

                        ### Get user input for action - Check Balance/ Exit
                        option = int(input("Enter the option: "))
                        while True:
                            if option == 1:
                                check_balance(account, login)
                                return False
                            elif option == 2:
                                return True
                            else:
                                option = int(input("Invalid input, please enter the option again: "))
            else:
                ### display input prompt for invalid input
                account_chosen_2 = input("Invalid input, please select the currency: ")
    return False
    
   

# welcome page

print("##################################################")
print("## {} ##".format("".center(width)))
print("## {} ##".format("Welcome to PyBank".center(width)))
print("## {} ##".format("".center(width)))
print("##################################################")
      
# Task 1: login validation

### get user login name
login = input("Login Name: ")

### check if login name exists
while login not in account:
    login = input("Invalid login name, please enter your login name again: ")
else:
    ### get user password
    password_entered = input("Please enter your password, "+str(3-login_tried)+" attempts remaining: ")
    login_tried += 1
    while True:
        ### check if password is correct within 3 attempts
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
