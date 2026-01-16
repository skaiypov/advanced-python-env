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
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(amount, "пополнено на счёт", self._owner)
        else:
            print("Сумма должна быть положительной")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Недостаточно средств")
        elif amount <= 0:
            print("Сумма должна быть положительной")
        else:
            self._balance -= amount
            print(amount, "снято со счёта", self._owner)

    def get_balance(self):
        print("Баланс", self._owner, ":", self._balance)
        return self._balance


class VIPAccount(BankAccount):
    def get_balance(self):
        print("Баланс", self._owner, ":", self._balance)
        print("Так как вы VIP клиент, переводы на другие банки для вас без комиссии")
        return self._balance



acc1 = BankAccount()
acc1._owner = "Мансур"
acc1._balance = 100000

acc2 = VIPAccount()
acc2._owner = "Ескендир"
acc2._balance = 50000

# Операции
acc1.deposit(20000)
acc1.withdraw(15000)

acc2.deposit(10000)
acc2.withdraw(20000)

acc1.get_balance()
acc2.get_balance()





