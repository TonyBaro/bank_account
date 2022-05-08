class BankAccount:

    all_accounts=[]

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough funds")
            return self
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f'current balance is {self.balance}',f'current interest rate is {self.int_rate}', sep="\n")
        return self

    def yield_interest(self):
        if self.balance <=0:
            print("you have no money")
            return self
        else:
            self.balance = self.balance + (self.balance * self.int_rate)
            return self

    @classmethod
    def all_balances(cls):
        for accounts in cls.all_accounts:
            print (f'balance:{accounts.balance}')

checking = BankAccount(0.01, 5000)
savings = BankAccount(0.04,400)

checking.deposit(200).deposit(50).deposit(250).withdraw(1500).yield_interest().display_account_info()
savings.deposit(10000).deposit(50).withdraw(500).withdraw(200).withdraw(50).withdraw(250).yield_interest().display_account_info()

BankAccount.all_balances()