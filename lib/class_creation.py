# A class representing a car with attributes make, model, and year.
class Car:

    #Initializes a Car object.
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        #Prints out the car's information
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")