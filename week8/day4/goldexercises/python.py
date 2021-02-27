


# Exercise 1: Bank Account
# Part I:

# Create a BankAccount class that contains the following attribute and methods:
# balance
# __init__ : initialize the attribute
# deposit : accepts a positive int and adds to balance, raise an Exception if the int is not positive.
# withdraw : accepts a positive int and deducts from balance, raise an Exception if not positive



# Part III: Expand the bank account class



# Add the following attributes to the BankAccount class:
# username
# password
# authenticated (default to False)
# Create a method authenticate : Accepts 2 strings, username and password. 
# Sets the authenticated boolean to True if the username and password provided match the objects attributes
# Edit withdraw and deposit to only work if authenticated is set to True,
#  if someone tries an action without being authenticated raise an Exception


class BankAccount():
    

    def __init__(self, username, password, balance):
        self.username = username
        self.balance = balance
        self.password = password
        self.authenticate = False       

    def authenticate1(self, username1, password1):
        if username1 == self.username and password1 == self.password:
            self.authenticate = True
            return True
        else:
            print("wrong username or password")

    def show_balance(self):
        print(f"your balance is {self.balance}")


    def deposit(self, amount= 0):
        if self.authenticate == True:     
            try:
                amount >= 0
                if amount >= 0:
                    print(f"Deposit of ${amount} in progres...")
                    self.balance += amount
                    print(f"you have now ${self.balance} in your account")
                else:
                    print("number must be positive")
            except:
                print("you  must put a number")
        else:
            print("authenticate your username and password")

    def withdraw(self, amount= 0):
        if self.authenticate == True:
            try:
                amount >= 0
                if amount >= 0:
                    print(f"Withdraw of ${amount} in progres...")
                    self.balance -= amount
                    print(f"you have now ${self.balance} in your account")
                else:
                    print("number must be positive")
            except:
                print("you  must put a number")
        else:
            print("authenticate your username and password")


bank1 = BankAccount("gaston", "kornfeld", 0)
# bank1.deposit(100)
# bank1.deposit(500)
# bank1.withdraw(-200)
# bank1.authenticate1("gaston", "kornfeld")
# bank1.deposit(100)
# bank1.deposit(500)
# bank1.withdraw(200)

# Part II : Minimum balance account
# Create a MinimumBalanceAccount that inherits from BankAccount
# Extend the __init__ and accept “minimum_balance” attribute/parameter with a default of 0
# Override the withdraw method to only allow withdrawing 
# if the action will leave the balance higher than minimum_balance,
#  raise an Exception if the action is invalid


# class MinimumBalanceAccount(BankAccount):

#     def __init__(self,username, password, balance, minimum_balance):
#         BankAccount.__init__(self, username, password, balance)
#         self.minimum_balance = minimum_balance

#     def withdraw(self, amount= 0):
#         try:
#             amount >= 0
#             if amount >= 0 and (self.balance - amount) >= self.minimum_balance:
#                 print(f"Withdraw of ${amount} in progres...")
#                 self.balance -= amount
#                 print(f"you have now ${self.balance} in your account")
#             else:
#                 print(f"your balance is {self.balance}, number must be positive, or minimum balance ({self.minimum_balance}) can not be passed.")
#         except:
#             print("you  must put a number")


# min_acc = MinimumBalanceAccount("gaston", "kornfeld", 0, 100)

# min_acc.deposit(1000)
# min_acc.withdraw(300)
# min_acc.withdraw(-300)
# min_acc.withdraw("a")
# min_acc.withdraw(300)
# min_acc.withdraw(300)




# Part IV: Create an ATM class

# __init__:
# Accepts account_list, try_limit
# Validates that account_list contains a list of BankAccount or MinimumBalanceAccount
# Hint: isinstance()
# Validates that try_limit is a positive number,
#  if you get invalid input raise an Exception but move along and set try_limit to 2
# Sets attribute current_tries = 0
# Calls the method show_main_menu

class Atm():

    def __init__(self, account_list, try_limit=2):
        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0
        
        if self.try_limit < 0 :
            print("try limit must be positive, set it to default : 2")
            self.try_limit = 2





# show_main_menu:
# Will start a while loop to display a menu letting a user select:
# Log in : Will take input from a user for username and password and call log_in() with that input
# Exit
        

    def show_main_menu(self):
        user_choise = ""
        while user_choise != "exit" and user_choise != "login": 
            user_choise = input("Please write login or exit: \n")
        if user_choise == "login":
            username = input("Please put your username: \n")
            password = input("Please put your password: \n")
            self.log_in(username, password)
        



# Method:
# log_in:
# Accepts username and password
# Checks username and password against all accounts in account_list
# If there is a match call the method show_account_menu and set current_tries to 0
# If there is not a match with any account increment the current tries by 1.
#  Let the user try again until the limit is reached. Once reached display a message saying they reached max tries and shutdown the program




    def log_in(self, username, password):
        current_tries = 5
        help_for_the_loop = True
        for bank_account in self.account_list:
            check_the_account = bank_account.authenticate1(username, password)
            if check_the_account:
                help_for_the_loop = False
                bank_account.show_balance()
                # print(f"Current tryies: {self.current_tries}, try limit: {self.try_limit}")
                self.show_account_menu(bank_account)
        
        # if help_for_the_loop:
        #     current_tries -= 1
        #     print(f"you have  {current_tries} tries")
        #     if current_tries >= 0:
        #         self.log_in(username, password)
            
        




# show_account_menu:
# Accepts a BankAccount or MinimumBalanceAccount.
#  Will start a loop giving the user the option to deposit, withdraw or log out.




    def show_account_menu(self, bannk_account):
        user_choise = ""
        while user_choise != "withdraw" and user_choise != "deposit" and user_choise != "logout": 
            user_choise = input("Please write deposit, to deposit \n withdraw \nor  logout: \n")
        if user_choise == "logout":
            self.show_main_menu()
        elif user_choise == "deposit":
            amount = int(input("how much you want to deposit: \n"))
            bannk_account.deposit(amount)
        elif user_choise == "withdraw":
            amount = int(input("how much you want to withdraw: \n"))
            bannk_account.withdraw(amount)
        self.show_account_menu(bannk_account)
            







bank2 = BankAccount("gaston", "secure", 1000000)
list_of_account = [bank1, bank2]


atm1 = Atm(list_of_account, 5)
# atm1.log_in("gaston", "secure")
atm1.show_main_menu()




