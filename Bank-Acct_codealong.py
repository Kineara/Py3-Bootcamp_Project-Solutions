# Establish an abstract Account class with attributes shared by all accounts
class Account:
    def __init__(self,acct_num,initial_deposit):
        self.acct_num = acct_num
        self.balance = initial_deposit
    
    # string method to return a string showing balance
    def __str__(self):
        return f'${self.balance:.2f}'
    
    # Universal method for deposits
    def deposit(self,deposit_amt):
        self.balance += deposit_amt
    
    # Universal method for withdrawals
    def withdraw(self,withdraw_amt):
        if withdraw_amt <= self.balance:
            self.balance -= withdraw_amt
        else:
            print("Insufficient capital, peasant.")    


# Establish a Checking Account class that inherits from Account and adds checking-specific traits
class Checking(Account):
    def __init__(self,acct_num,initial_deposit):
        # super() refers to the base class and allows us to run parent class functions
        super().__init__(acct_num,initial_deposit)
    
    # define a string to return a checking account specific balance
    def __str__(self):
        return f"Checking Account #{self.acct_num}\nCurrent Balance: {Account.__str__(self)}"


# Establish Savings and Business account classes
class Savings(Account):
    def __init__(self,acct_num,initial_deposit):
        super().__init__(acct_num,initial_deposit)
        
    def __str__(self):
        return f"Savings Account #{self.acct_num}\nCurrent Balance: {Account.__str__(self)}"
    
class Business(Account):
    def __init__(self,acct_num,initial_deposit):
        super().__init__(acct_num,initial_deposit)
    
    def __str__(self):
        return f"Business Account #{self.acct_num}\nCurrent Balance: {Account.__str__(self)}"
    

# Establish a customer class that holds name, pin, and any number of account objects
class Customer:
    def __init__(self,name,pin):
        self.name = name
        self.pin = pin
        
    # dictionary to hold all accounts
        self.accts = {'checking':[],'business':[],'savings':[]}
        
    def __str__(self):
        return self.name
        
    def new_checking(self,acct_num,initial_deposit):
        self.accts['checking'].append(Checking(acct_num,initial_deposit))
        
    def new_business(self,acct_num,initial_deposit):
        self.accts['business'].append(Business(acct_num,initial_deposit))
    
    def new_savings(self,acct_num,initial_deposit):
        self.accts['savings'].append(Savings(acct_num,initial_deposit))
        
    # method to return balances and total funds
    def get_total(self):
        total = 0
        
        for account in self.accts['checking']:
            total += account.balance
            print(account)
        for account in self.accts['business']:
            total += account.balance
            print(account)
        for account in self.accts['savings']:
            total += account.balance
            print(account)
        
        print(f"Combined account funds: ${total:.2f}")
        

# functions for withdrawals and deposits
def make_dep(cust,acct_type,acct_nbr,dep_amt):
    """
    make_dep(cust,acct_type,acct_num,dep_amt)
    cust = variable name (customer name/ID)
    acct_type = string 'savings', 'checking', or 'business'
    acct_num = integer
    dep_amt = integer
    """
    for account in cust.accts[acct_type]:
        if account.acct_num == acct_nbr:
            account.deposit(dep_amt)


def make_withdrawal(cust,acct_type,acct_nbr,dep_amt):
    """
    make_dep(cust,acct_type,acct_num,dep_amt)
    cust = variable name (customer name/ID)
    acct_type = string 'savings', 'checking', or 'business'
    acct_num = integer
    dep_amt = integer
    """
    for account in cust.accts[acct_type]:
        if account.acct_num == acct_nbr:
            account.withdraw(dep_amt)
            