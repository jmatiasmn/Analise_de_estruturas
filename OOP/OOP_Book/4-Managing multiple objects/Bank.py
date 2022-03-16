from Account import *

class Bank():

    def __init__(self):
        self.accountsDict = {}
        self.nextAccountNumber = 0
    
    def createAccount(self,theName,theStartingAmount,thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber
        self.accountsDict[newAccountNumber] = oAccount
        #Next account
        self.nextAccountNumber = self.nextAccountNumber + 1
        return newAccountNumber
    
    def openAccount(self):
        print('*** Open Account ***')
        userName = input('What is the name for the new user account? ')
        userStartingAmount = int(input('What is the starting balance for this account? '))
        userPassword = input('What is the password you want to use for this account? ')
        nextAccountNumber = self.createAccount(userName, userStartingAmount, userPassword)
        print('Your new account number is:', nextAccountNumber)
        print()
    
    def balance(self):
        print('*** Get Balance ***')
        userAccountNumber = int(input('Please enter your account number: '))
        oAccount = self.accountsDictaccountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountNumber)
        if theBalance is not None:
            print('Your balance is: ', theBalance)

    def deposit(self):
        print('*** Deposit ***')
        userAccountNumber = int(input('Please enter the account number: '))
        userDepositAmount = int(input('Please enter amount to deposit:        '))
        userPassword = input('Please enter the password: ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.deposit(userDepositAmount, userPassword)

    def show(self):
        print('Show:')
        for userAccountNumber in accountsDict:
            oAccount = accountsDict[userAccountNumber]
            print('Account number: ', userAccountNumber) 
            oAccount.show()
    
    def withdraw(self):
        print('*** Withdraw ***')
        userAccountNumber = int(input('Please enter your account number: '))
        userWithdrawalAmount = int(input('Please enter the amount to withdraw: '))
        userPassword = input('Please enter the password: ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.withdraw(userWithdrawalAmount, userPassword)
        if theBalance is not None:
            print('Withdrew:', userWithdrawalAmount)
            print('Your new balance is:', theBalance)
        else:
            print('Sorry, that was not a valid action. Please try again.')


    def closeaccount(self):
        pass