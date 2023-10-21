import BankManager

'''
The Bank Manager application consists of three Python files:
Bankmanager.py, Banker.py, and BankAccount.py. 
The main method is located in Banker.py, which serves as the entry point for the application.

The application allows users to manage their bank accounts, including savings and checking accounts. 
Users can view the total amount of money in their accounts, withdraw money, and 
receive notifications when their accounts are overdrawn.

The BankAccount.py file contains a BankAccount class that serves as a
 template for creating bank accounts. 
The class contains attributes such as the account balance, account type, and account number, and 
methods such as deposit, withdraw, and get_balance.

The Banker.py file imports the BankAccount class from the BankAccount.py file 
and uses it to create instances of bank accounts for users. It contains methods for 
displaying account information, 
withdrawing money, and checking for overdrafts.

Overall, the Bank Manager application provides users with a convenient way to 
manage their bank accounts and keep track of their finances.

'''

#Created By @MdBillah

def main():
    #BankManager is package, BankManager() is a class and bm instance of BankManager class

    bm = BankManager.BankManager()

    op = ''
    while op != 'Q':
        print('\nHere are the possible commands for managing your bank:')
        print('\tQ - Quit the program')
        print('\tN - start a New day')
        print('\tA - list all Accounts, their balances, ' +
              'and the bank\'s total funds')
        print('\tC - open a new Checking account')
        print('\tS - open a new Savings account')
        print('\tD - make a Deposit into an account')
        print('\tW - make a Withdrawal from an account')
        op = input('What is your command?  ').upper()
        
        if op == 'N':
            # start a New day
            bm.newDay()
        elif op == 'A':
            # list all Accounts, their balances, and the bank's total funds
            bm.listAccounts()
        elif op == 'C':
            # open a new Checking account
            bm.openChecking()
        elif op == 'S':
            # open a new Savings account
            bm.openSavings()
        elif op == 'D':
            # make a Deposit into an account
            bm.makeDeposit()
        elif op == 'W':
            # make a Withdrawal from an account
            bm.makeWithdrawal()
        elif op != 'Q':
            # Unknown command
            print('Sorry, but %s is an unknown command.' % op)

if __name__ == '__main__':
    main()
