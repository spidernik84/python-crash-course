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


class Battery:
    """ Simple class to model a car battery """

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def get_range(self):
        """ Print statement about battery range """
        if self.battery_size == 75:
            car_range = 260
        elif self.battery_size == 100:
            car_range = 315
        
        print(f"This car can run for {car_range} miles.")

    def describe_battery(self):
        """ Describe the features of the battery """
        print(f"This car has a battery size of {self.battery_size}-kWh.")
    
    def upgrade_battery(self):
        """ Upgrades battery to 100kWh """
        if self.battery_size != 100:
            self.battery_size = 100

class ElectricCar(Car):
    """ Represents characteristics specific to an electric car """

    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        self.battery = Battery()



my_new_car = Car('audi','a4',2009)

print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(25)
my_new_car.read_odometer()
my_new_car.increment_odometer(10)
my_new_car.read_odometer()


my_tesla = ElectricCar('tesla','model s', 2019)

print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


upgraded_tesla = ElectricCar('tesla', 'model x', 2018)

upgraded_tesla.battery.describe_battery()
upgraded_tesla.battery.get_range()
upgraded_tesla.battery.upgrade_battery()
upgraded_tesla.battery.describe_battery()
upgraded_tesla.battery.get_range()
