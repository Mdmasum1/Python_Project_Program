import BankAccount


#Created By @MdBillah

INTEREST_RATE = 0.04

TRANSACTION_CHARGE = 0.25
OVERDRAFT_FEE = 10

MIN_DEPOSIT_TO_UNLOCK = 25

# return a properly formatted currency string
def currency(amount):
    if amount < 0.0:
        return '-$' + '{:,.2f}'.format(abs(amount))
    else:
        return '$' + '{:,.2f}'.format(amount)
    
class BankManager():

    # constructor
    def __init__(self):
        self.accounts = []
    
    # given an account number, return the associated account or None if there
    # is no account with that number
    def find_account(self, ID):
        for account in self.accounts:
            if account.getID() == ID:
                return account
        return None
    
    
    # advance the time by one day by adding interest to every savings
    # account that is not overdrawn
    def newDay(self):
        for account in self.accounts:
            balance = account.getBalance()
            if (account.getType() == BankAccount.SAVINGS) and (balance > 0.0):
                   
                account.deposit(balance * (INTEREST_RATE / 365))

    # list all the accounts and their current balances.  Also show the total
    # funds held in the bank's account
    def listAccounts(self):
        assets = 0.0
        for account in self.accounts:
            balance = account.getBalance()
            assets += balance
            print('  ', account.getID(), ':  type = ', account.getType(),
                  '\tbalance = ', currency(balance), sep='', end = '')
            if account.isLocked():
                print('\tLOCKED')
            else:
                print()
        print('  ***** Total bank assets =', currency(assets), '*****')

    # open a new checking account            
    def openChecking(self):
        account = BankAccount.BankAccount(BankAccount.CHECKING)
        self.accounts.append(account)
        print('  Checking account', account.getID(), 'opened.')

    # open a new savings account
    def openSavings(self):
        account = BankAccount.BankAccount(BankAccount.SAVINGS)
        self.accounts.append(account)
        print('  Savings account', account.getID(), 'opened.')

    # make a deposit
    # If the account is locked and deposit is large enough, the account is
    # unlocked
    def makeDeposit(self):
        ID = int(input('  Into which account?  '))
        account = self.find_account(ID)
        if account == None:
            print('  No such account')
        else:
            amount = float(input('  Amount of deposit:  $'))
            account.deposit(amount)
            account.withdrawal(TRANSACTION_CHARGE)
            print('  Deposit successful.  New balance =',
                  currency(account.getBalance()))
            if account.isLocked() and (amount >= 25.00):
                account.unlock()
                print('  THIS ACCOUNT IS NOW UNLOCKED.')

    # make a withdrawl
    # Accounts can only be made into an unlocked account.
    # If the attempted withdrawal is larger than the account's current balance,
    # the account is locked and is charged an overdraft fee.
    def makeWithdrawal(self):
        ID = int(input('  From which account?  '))
        account = self.find_account(ID)
        if account == None:
            print('  No such account')
        elif account.isLocked():
            print('  This account has been locked due to an overdraft attempt.')
            print('  No withdrawals are currently allowed.')
        else:
            amount = float(input('  Amount of withdrawal:  $'))
            if amount + TRANSACTION_CHARGE <= account.getBalance():
                account.withdrawal(amount)
                account.withdrawal(TRANSACTION_CHARGE)
                print('  Withdrawl successful.  New balance =',
                      currency(account.getBalance()))
            else:
                print('  Account balance insufficent for requested withdrawal.')
                account.withdrawal(OVERDRAFT_FEE)
                account.lock()
                print('  THIS ACCOUNT IS NOW LOCKED FROM FURTHER WITHDRAWALS.')
