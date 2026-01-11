# Task 5. OOP Principles & Custom Classes
#
#  Create a class BankAccount with:
#
#  Private attributes __balance and __owner
#
#  Methods:
#  - deposit(amount)
#  - withdraw(amount)
#  - get_balance()
#
#  Validate input:
#  - Deposit must be positive
#  - Withdrawal must not exceed balance


class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            print(amount, "тенге пополнено. Баланс:", self.__balance, "тенге")
        else:
            print("Невозможно пополнить", amount, "тенге, сумма должна быть положительной")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Не удалось снять", amount, "тенге, недостаточно средств. Баланс:", self.__balance, "тенге")
        elif amount <= 0:
            print("Невозможно снять", amount, "тенге, сумма должна быть положительной")
        else:
            self.__balance = self.__balance - amount
            print(amount, "тенге списано. Баланс:", self.__balance, "тенге")

    def get_balance(self):
        return self.__balance


acc1 = BankAccount("Мансур", 100000)
acc2 = BankAccount("Ескендир", 50000)

acc1.deposit(20000)
acc1.withdraw(15000)
acc2.withdraw(60000)
acc2.deposit(-5000)
acc2.withdraw(-10000)

print()
print("Баланс Мансура:", acc1.get_balance(), "тенге")
print("Баланс Ескендира:", acc2.get_balance(), "тенге")


