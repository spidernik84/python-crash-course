from car import Car

my_new_car = Car('audi','a6',2020)

print(my_new_car.get_descriptive_name())

my_new_car.odometer_mileage = 23
my_new_car.read_odometer()