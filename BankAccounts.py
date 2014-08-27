#Name: David Mamujee
#Date: October 23, 2013
#Description: A program that will allow users to create bank accounts and deposit and withdraw money from them.

import random
#Converts values into the currency format
def currencyFormat(number):    
    output = "{:,.2f}".format(number)
    output = "$" + output
    return output
#Checks if input is string
def intCheck(Input):
    try:
        float(Input)
    except ValueError:
        return False
    else:
        return True

class BankAccount():
    #Gives person balance of 0 when account is initialized
    balance = 0

    #Deposits given amount into user's account
    def deposit(self,amount):
        if intCheck(amount) == False:
            print("Invalid Input")
        else:
            self.balance = self.balance + amount

    #Withdraws given amount from user's account    
    def withdraw(self, amount):
        if intCheck(amount) == False:
            print("Invalid Input")
        elif amount > self.balance:
            print("Insufficent Funds")
        else:
            self.balance = self.balance - amount
        
    #Returns balance of user's account
    def checkBalance(self):
        return currencyFormat(self.balance)

    #Takes all money from the balance of accounts in list, and put it into own account
    def robTheBank(self,accounts):
        total = 0
        #Counts how much money is in each account, and then sets the account balance to 0
        for i in accounts:
            total = total + i.balance
            i.balance = 0
        #Puts all the stolen money in own account
        self.balance = total
        print("You have stolen",currencyFormat(total))

    #Takes 10% of own account and gives it to a new created account for child
    def childAccount(self):
        child = BankAccount()
        #Gives 10% of balance to child
        child.balance = self.balance*0.1
        self.balance = self.balance - child.balance
        return child

#Testing Log        

user1 = BankAccount()
#Deposists $100 into user1's account
user1.deposit(100)
user1.deposit("One Hundred")
print (user1.checkBalance())
#Trys to withdraw different amounts from user1's account
user1.withdraw(150)
user1.withdraw(50.50)
user1.withdraw("Fifty")
print(user1.checkBalance())

#Creates 5 account instances
loop1 = BankAccount()
loop2 = BankAccount()
loop3 = BankAccount()
loop4 = BankAccount()
loop5 = BankAccount()

#Puts each of the previously mentioned accounts into a list
List = [loop1,loop2,loop3,loop4,loop5]
#Each item in list is given a random amount of money between $0 and $1,000,000
for i in List:
    i.deposit(random.randint(0,1000000))
    #Prints how much money is in each account
    print(i.checkBalance())

#Bank is robbed
bankRobber = BankAccount()
bankRobber.robTheBank(List)
print(bankRobber.checkBalance())

#Checks to see if robbed accounts are empty
for i in List:
    print(i.checkBalance())

#Creates an account for the bank robber's baby
babyBankRobber = bankRobber.childAccount()
#Prints new balances
print(babyBankRobber.checkBalance())
print(bankRobber.checkBalance())
