from restaurant import Restaurant

nicos_italian = Restaurant("Nico's Italian","italian")

nicos_italian.describe_restaurant()
nicos_italian.restaurant_open()

print(nicos_italian.customers_served(4))

print(nicos_italian.increment_customers(1))
