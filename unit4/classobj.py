#Example of Class & Obj

class Bike:
    wheels = 2
    def __init__(self, brand, model):
        self.brand = brand 
        self.model = model 

    def show_info(self):
        print(f"This is a {self.brand} {self.model} with {Bike.wheels} wheels.")
my_bike = Bike("Hero", "Splender")
my_bike.show_info()


#OUTPUT
#This is a Hero Splender with 2 wheels.
