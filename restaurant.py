""" Simple class to model a restaurant """

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