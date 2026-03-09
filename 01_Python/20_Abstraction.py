from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(amount):
        pass

class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        print(f"Paying {amount} via Credit Card")
    
class Paypal(PaymentMethod):
    def process_payment(self, amount):
        print(f"Paying {amount} via Paypal")
        
class Jazzcash(PaymentMethod):
    def payment(self, amount):
        print(f"Paying {amount} via Jazzcash")
        
payment_method = [CreditCard(), Paypal()]

for method in payment_method:
    method.process_payment(500)
    
# jazzcash = Jazzcash().payment(500)    # It Will through error because Abstract Classes Must Implement Abstract Method - In this ( process_payment ) is not implemented
    
