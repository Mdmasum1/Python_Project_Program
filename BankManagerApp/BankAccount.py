
# Created by @MdBillah
# Account types to pass as argument to the constructor
CHECKING = 'checking'
SAVINGS  = 'savings '

class BankAccount(object):

    # The next available account number
    ACCOUNT_NUMBER = 1000
    
    # constructor
    def __init__(self, account_type, initial_balance = 0.0):
        self.ID = BankAccount.ACCOUNT_NUMBER
        BankAccount.ACCOUNT_NUMBER += 1
        self.account_type = account_type
        self.balance = initial_balance
        self.locked = False

    # get the account type (checking or savings)
    def getType(self):
        return self.account_type

    # get the account's ID
    def getID(self):
        return self.ID

    # make a deposit into the account
    def deposit(self, amount):
        self.balance += amount

    # make a withdrawal from the account
    # Before making a withdrawal, the caller should check that sufficent funcs
    # are available using the check_balance function.
    def withdrawal(self, amount):
        self.balance -= amount

    # get the account's balance
    def getBalance(self):
        return self.balance

    # lock the account (for an attempt to overdraw)
    def lock(self):
        self.locked = True

    # unlock the account (after sufficient deposit)
    def unlock(self):
        self.locked = False
        
    # check whether an account is locked
    def isLocked(self):
        return self.locked
