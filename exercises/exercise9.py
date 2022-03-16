# 8-3 T-Shirt try it yourself

def make_shirt(size, msg):
    print(size + ' = ' + msg)

# make_shirt('medium', 'wsu shockers')
# make_shirt(size='t shirt is a medium', msg='t shirt says wsu shockers')

# 8-4 Large shirts:
make_shirt('size', 'msg')
print('t-shirts' + ' = ' + 'large')
print('wsu shockers' + ' = ' + 'medium')

# make_shirt(size='large', msg='i love python')
# make_shirt(size='medium', msg='wsu shockers')
# 8-5 Cities


def describe_city(country = 'iceland'):
    print('vik is in' ' ' + country)
    print('reykjavik is in' ' ' + country)
    print('akureyri is in')


# describe_city(country='iceland')

# 8-9 Messages:
short_msgs = 'have a nice day', 'talk to you later!'

def show_messages():
    print(short_msgs)

# show_messages()

# 8 - 10 & 8-11
sent_messages = {short_msgs}, \
                {'how was your day? did you have a good day?'}

def send_messages():
    print(sent_messages)

# send_messages()



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

    def set_numer_served(self, customers):
        self.number_served = customers

    def increment_number_served(self, increment):
        self.number_served += increment







# pizza_restaurant = Restaurant('Pizza hut', 'american italian')
# sushi_restaurant = Restaurant('wasabi', 'japanese')
# tacos_restaurant = Restaurant('tacos tj', 'mexican')
# print(f"restaurant_name:{pizza_restaurant.restaurant_name}")
# print(f"restaurant_cuisine:{pizza_restaurant.cuisine_type}")
# print(f"restaurant_name: {sushi_restaurant.restaurant_name}")
# print(f"restaurant_cuisine: {sushi_restaurant.cuisine_type}")
# print(f"restaurant_name: {tacos_restaurant.restaurant_name}")
# print(f"restaurant_cuisine: {tacos_restaurant.cuisine_type}")
# restaurant = Restaurant('chick-fil-a', 'american')
# print(f"restaurant_name: {restaurant.restaurant_name}")
# print(f"restaurant_cuisine: {restaurant.cuisine_type}")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# 9-3
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

    def increment_login_attempt(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0



# users = user('omar', 'munoz', 23, 'cloud applications')
# users.describe_user()
# users.greet_user()

# 9-4
restaurant = Restaurant('chick-fil-a', 'american')
# print(f"number served: {restaurant.number_served}")

restaurant.number_served = 100
# print(f"number served: {restaurant.number_served}")

restaurant.set_numer_served(150)
# print(f"number served: {restaurant.number_served}")

restaurant.increment_number_served(175)
# print(f"number served: {restaurant.number_served}")

# 9-5
users = user('omar', 'munoz', 23, 'cloud applications')
user.increment_login_attempt()
print(f"login attempts: {user.login_attempts}")

user.reset_login_attempts()
print(f"login attempts reset: {user.login_attempts}")

