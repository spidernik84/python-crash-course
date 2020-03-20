class User:
    def __init__(self,first_name,last_name,age,nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, of age {self.age}, is {self.nationality}")
    
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, welcome.")


class Admin(User):
    def __init__(self, first_name, last_name, age, nationality):
        super().__init__(first_name, last_name, age, nationality)
        self.privileges = ('Write','Remove','Update')
    
    def describe_privileges(self):
        for priv in self.privileges:
            print(priv)


nico = User("Nicola","Volpini",36,"Italian")

nico.describe_user()
nico.greet_user()
        

god = Admin("God","Almighty",3000,"Palestinian")

god.describe_user()
god.greet_user()
god.describe_privileges()
