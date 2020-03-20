class Restaurant:
    def __init__(self,name,cuisine):
        self.name = name
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        print(f"{self.name} serves fine {self.cuisine} cuisine")

    def customers_served(self,customers):
        self.served_customers = customers
        return self.served_customers
    
    def increment_customers(self, customers):
        self.served_customers += customers
        return self.served_customers

    def restaurant_open(self):
        print(f"{self.name} is open!")


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        """ import superclass restaurant """
        super().__init__(name, cuisine)
        self.available_flavors = ('chocolate','Vanilla')
    
    def list_available_flavors(self):   
        print("Here are the available flavors:")
        for flavor in self.available_flavors:
            print(flavor)



nicos_italian = Restaurant("Nico's Italian","italian")

nicos_italian.describe_restaurant()
nicos_italian.restaurant_open()

print(nicos_italian.customers_served(4))

print(nicos_italian.increment_customers(1))


nicos_gelato = IceCreamStand("Nico's Gelato","Gelato")

nicos_gelato.list_available_flavors()
