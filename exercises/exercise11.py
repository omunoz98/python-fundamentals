# 9-6
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Closes on sundays {self.restaurant_name}")
        print(f"The cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open, expect sundays")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display(self):
        print('The flavors are')
        for flavor in self.flavors:
            print(f"{flavor}")

# ice_cream = IceCreamStand('vanilla', 'chocolate', 'strawberry')
# ice_cream.display()

#9-7

class user:


    def __init__(self, first_name, last_name, age, major):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.major = major
        self.login_attempts = 0

    def describe_user(self):
        print(f"This users name is {self.first_name} {self.last_name}.")
        print(f"I am {self.age} and my major is {self.major}.")

    def greet_user(self):
        print(f"Hi {self.first_name} {self.last_name}")

class admin(user):

    def __init__(self, first_name, last_name, age, major, privileges):
        super().__init__(first_name, last_name, age, major)
        self.first_name = first_name
        self.age = age
        self.major = major
        self.privileges = privileges(privileges)


    def show_privileges(self):
        print('privileges')
        for privilege in self.privileges:
            print(f"{privilege}")
# admin1 = admin('Omar', 'Munoz', 23, 'cloud', "can add post, can delete post, can ban user")
# admin1.show_privileges()

#9-8

class privileges:

    def __init__(self, first_name, last_name, age, major, privileges):
        super().__init__(first_name, last_name, age, major)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.major = major
        self.privileges = privileges




