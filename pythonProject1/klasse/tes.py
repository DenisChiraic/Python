class NoMoney(Exception):
    def __init__(self, message: str):
        self.message = message
    pass


class BankAccount:
    def __init__(self,owner: str, amount = 0):
        self.owner = owner
        self.amount = amount

    def withdraw(self, num: int):
        if num <= self.amount:
            self.amount -= num
            return self.amount
        else:
            raise NoMoney("You have not enough money")

class CreditBankAccount(BankAccount):
    def __init__(self, owner, amount = 0 , credit_score = 1):
        BankAccount.__init__(self, owner = owner, amount = amount)
        self.credit_score = credit_score

    def withdraw(self, num: int):
        try:
            x = BankAccount(owner=self.owner, amount=self.amount)
            x.withdraw(num)
            self.credit_score += 1
        except NoMoney:
            self.credit_score -= 1

    def __add__(self, other):
        return CreditBankAccount(owner = self.owner, amount = self.amount + other.amount, credit_score = self.credit_score + other.credit_score)

    def __repr__(self):
        return f"Owner: {self.owner}, Amount: {self.amount}, Credit Score:{self.credit_score}"

def main():
    # x = BankAccount("BOB")
    # x.amount = 1000
    # x.withdraw(10)
    # print(x.amount)

    x = CreditBankAccount("Bob")
    y = CreditBankAccount("Dob")
    x.amount = 300
    y.amount = 600
    print(x.credit_score)
    x.withdraw(200)
    print(x.credit_score)
    print(y+x)

main()

def my_func(n):
    if n in (0, 1):
        return n

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

def myfunc(n):
    if n in (0, 1):
        return n
    else:
        return myfunc(n - 2) + myfunc(n - 1)

#print(my_func(6))
#print(myfunc(6))