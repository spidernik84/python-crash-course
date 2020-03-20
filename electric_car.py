from car import Car

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


class ElectricCar(Car):
    """ Represents characteristics specific to an electric car """

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
