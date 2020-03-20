from car import Car
from electric_car import ElectricCar

my_new_car = Car('bmw','m3',2018)

print(my_new_car.get_descriptive_name())

my_new_elcar = ElectricCar('Tesla','Roadster',2016)

print(my_new_elcar.get_descriptive_name())