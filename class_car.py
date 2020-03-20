class Car:
    """ Simple car class """

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_mileage = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"Car has {self.odometer_mileage} miles on it")

    def update_odometer(self,mileage):
        """ Set the mileage of your car """
        if mileage >= self.odometer_mileage:
            self.odometer_mileage = mileage
        else:
            print("You can't rollback the mileage...")
    
    def increment_odometer(self,increment):
        """Increment miles"""
        self.odometer_mileage += increment

my_new_car = Car('audi','a4',2009)

print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(25)
my_new_car.read_odometer()
my_new_car.increment_odometer(10)
my_new_car.read_odometer()