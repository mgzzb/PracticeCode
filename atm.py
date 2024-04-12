class ATM:

    def __init__(self):
        self.banknotes = [0]*5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(self.banknotes)):
            self.banknotes[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        val = [20, 50, 100, 200, 500]
        money = [0]*5

        for i in range(4,-1,-1):
            count = min(self.banknotes[i], amount // val[i]) 
            money[i] += count
            amount -= count * val[i] 

        if amount == 0:
            self.banknotes = [x-y for x, y in zip(self.banknotes, money)]
            return money
            
        return [-1]
               


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
