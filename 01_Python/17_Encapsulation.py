class BankAccount:
    
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        
    def deposit(self, amount_to_deposit):
        if amount_to_deposit > 0:
            print(f"Dear {self.name}! {amount_to_deposit} added to your bank account")
            self.__balance += amount_to_deposit
        else:
            print("Please deposit valid amount")
            
    def withdraw(self, amount_to_withdraw):
        if self.__balance > amount_to_withdraw:
            self.__balance -= amount_to_withdraw
            print(f"{self.name} Rs.{amount_to_withdraw} withdrawl from your account")
        else:
            print("Insuficient Funds")
            
    def check_balance(self):
        print(f"{self.name} your current balance is Rs.{self.__balance}")
    
    def get_balance(self):
        balance = self.__balance
        return balance           

user_name = input("Enter your account name: ")
initial_balance = int(input("Enter your initial deposit amount: "))
    
Ali = BankAccount(user_name, initial_balance)

Ali.check_balance()
Ali.deposit(2000)
Ali.withdraw(3000)
Ali.check_balance()



