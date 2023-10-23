class Account:
    def __init__(self, number, name, balance):
        self.__number = number
        self.__name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount at Deposit")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance: 
            self.balance -= amount
        else:
            print("Invalid amount at withdraw")
            
    def get_balance(self):
        return self.__balance
    
    def updata_balance(self, balance):
        self.__balance = balance
        
class Savings(Account):
    def __init__(self, number, name, balance, interest_rate):
        super().__init__(number, name, balance)
        self.__interest_rate = interest_rate
    def calculate_interest(self):
        monthly_interest = (self.interest/12) * self.__balance
        self.__balance = self.__balance + monthly_interest
        
if __name__ == '__main__':
    test_account = Savings(1, 'Joe', 5, 0.12)
    test_account.deposit(5)