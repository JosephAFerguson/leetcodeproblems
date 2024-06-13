class Bank:
    an = []
    def __init__(self, balance: List[int]):
        self.an = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        account1-=1
        account2-=1
        if account1 < 0 or account1 >= len(self.an) or account2 < 0 or account2 >= len(self.an) :
            return False
        if self.an[account1] < money or money < 0:
            return False
        self.an[account1] -= money
        self.an[account2] += money
        return True


    def deposit(self, account: int, money: int) -> bool:
        account-=1
        if account >=0 and account < len(self.an):
            self.an[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        account-=1
        if account >=0 and account < len(self.an):
            if self.an[account] >= money:
                self.an[account] -= money
                return True
        return False

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
