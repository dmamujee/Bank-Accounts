# Name: David Mamujee
# Date: October 23, 2013
# Description: A program that will allow users to create bank accounts and deposit and withdraw money from them.

import random


# Converts values into the currency format
def currency_format(number):
    output = "{:,.2f}".format(number)
    output = "$" + output
    return output


# Checks if input is string
def int_check(given_input):
    try:
        float(given_input)
    except ValueError:
        return False
    else:
        return True


class BankAccount:
    def __init__(self):
        pass

    # Gives person balance of 0 when account is initialized
    balance = 0

    # Deposits given amount into user's account
    def deposit(self, amount):
        if not int_check(amount):
            print("Invalid Input")
        else:
            self.balance = self.balance + amount

    # Withdraws given amount from user's account
    def withdraw(self, amount):
        if not int_check(amount):
            print("Invalid Input")
        elif amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount

    # Returns balance of user's account
    def check_balance(self):
        return currency_format(self.balance)

    # Takes all money from the balance of accounts in list, and put it into own account
    def rob_the_bank(self, accounts):
        total = 0
        # Counts how much money is in each account, and then sets the account balance to 0
        for i in accounts:
            total += i.balance
            i.balance = 0
        # Puts all the stolen money in own account
        self.balance = total
        print("You have stolen", currency_format(total))

    # Takes 10% of own account and gives it to a new created account for child
    def child_account(self):
        child = BankAccount()
        # Gives 10% of balance to child
        child.balance = self.balance * 0.1
        self.balance = self.balance - child.balance
        return child


# Testing Log

user1 = BankAccount()
# Deposits $100 into user1's account
user1.deposit(100)
user1.deposit("One Hundred")
print (user1.check_balance())
# Tries to withdraw different amounts from user1's account
user1.withdraw(150)
user1.withdraw(50.50)
user1.withdraw("Fifty")
print(user1.check_balance())

# Creates 5 account instances
loop1 = BankAccount()
loop2 = BankAccount()
loop3 = BankAccount()
loop4 = BankAccount()
loop5 = BankAccount()

# Puts each of the previously mentioned accounts into a list
List = [loop1, loop2, loop3, loop4, loop5]
# Each item in list is given a random amount of money between $0 and $1,000,000
for item in List:
    item.deposit(random.randint(0, 1000000))
    # Prints how much money is in each account
    print(item.check_balance())

# Bank is robbed
bankRobber = BankAccount()
bankRobber.rob_the_bank(List)
print(bankRobber.check_balance())

# Checks to see if robbed accounts are empty
for item in List:
    print(item.check_balance())

# Creates an account for the bank robber's baby
babyBankRobber = bankRobber.child_account()
# Prints new balances
print(babyBankRobber.check_balance())
print(bankRobber.check_balance())
