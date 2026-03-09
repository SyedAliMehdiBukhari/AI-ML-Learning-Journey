class Car:
    def __init__(self, brand_name, model):
        self.brand = brand_name
        self.model = model
        
    def drive(self):
        print(f"Driving the {self.brand} {self.model}")
        
class ElectricCar(Car):
    
    def charge(self):
        print("Battery is charging")
        
electricCar = ElectricCar("Toyota", "Prius")

electricCar.drive()
electricCar.charge()