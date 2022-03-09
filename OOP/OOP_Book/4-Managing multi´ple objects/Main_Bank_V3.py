from Account import *

accountsDict = {}

nextAccountNumber = 0

#Create two accounts

oAccount = Account('Joe', 100, 'JoesPassword')
joesAccountNumber = nextAccountNumber
accountsDict[joesAccountNumber] = oAccount
print('Account number for Joe is:', joesAccountNumber)

oAccount = Account('Mary', 12345, 'MarysPassword')
marysAccountNumber = nextAccountNumber + 1
accountsDict[marysAccountNumber] = oAccount
print('Account number for Mary is:', marysAccountNumber)

nextAccountNumber+=1

accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()
print()


#Call some methods on the different accounts

print('Calling methods of the two accounts')
accountsDict[joesAccountNumber].deposit(50, 'JoesPassword')
accountsDict[marysAccountNumber].withdraw(345, 'MarysPassword')
accountsDict[marysAccountNumber].deposit(100,'MarysPassword')

#show the accounts
accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()

#Create another account with information from the user
print()
userName = input('What is the name for the new user account? ')
userBalance = int(input('What is the starting balance for this account? '))
userPassword = input('What is the password you want to use for this account? ')
oAccount = Account(userName, userBalance, userPassword)
newAccountNumber = nextAccountNumber
accountsDict[newAccountNumber] = oAccount
print('Account number for new account is:',newAccountNumber)
nextAccountNumber +=1

#show the newly created user account

accountsDict[newAccountNumber].show()

#Let's deposit 100 into the new account

accountsDict[newAccountNumber].deposit(100, userPassword)
userBalance = accountsDict[newAccountNumber].getBalance(userPassword)
print()
print("After depositing 100, the user's balance is:", userBalance)

#Show the new account
accountsDict[newAccountNumber].show()