# 1.On page 78 of your book, do 5-1 of the Try it Yourself.
# Put all your code in your exercise5.py file.
# 2. On page 78 of your book, create new examples that meet the bullet points of 5-2.
# Put your code for this in your exercise5.py file.
# 3.Write a function that will take 2 arguments.
# Inside the function provide examples of all the arithmetic operators.
# Provide a variable for each solution and print the results of each.
# 4.Write a function that takes only 1 argument.
# Inside the function provide examples of:
# Assignment operators: modulus equals, minus equals, exponent equals & plus equals.
# Provide a variable for each solution and print the results of each.


shoe = 'nike'
print("Shoes are == 'nike'? I predict True.")
print(shoe == 'nike')

print("\nIs shoes == 'adidas'? I predict False.")
print(shoe == 'adidas')



dog = 'small'
print("dog is == 'small'")
print(dog == 'small')

print("\nthe dog == 'big'?")
print(dog == 'big')


car = 'ford'
print("car is == 'ford'")
print(car == 'ford')

print("\ncar is == 'chevy'")
print(car == 'chevy')


coffee = 'starbucks'
print("coffee is == 'starbucks'")
print(coffee == 'starbucks')

print("\ncoffee is == 'scooters'")
print(coffee == 'scooters')


phone = 'apple'
print("phone is == 'apple'")
print(phone == 'apple')

print("\nphone is == 'galaxy'")
print(phone == 'android')


# 5-2
def equal_inequal(num1, num2):
    result_equal = num1 == num2
    print(result_equal)
    result_not = num1 != num2
    print(result_not)


# equal_inequal('TRUE', 'true')


    result_equal = num1.lower == num2
    print(result_equal)
    result_not = num1.lower() != num2
    print(result_not)


# equal_inequal('num', 'NUM')


alpha = 15
omega = 25

def greater():
    great = alpha < omega
    great1 = alpha > omega
    print(great)
    print(great1)


# greater()


def logic_and():
    result = alpha > 10 and omega > 20
    print(result)


# logic_and()


def logic_or(num):
    result = omega > num or num < alpha
    print(result)


# logic_or(20)


supra = "2jz are cool"


def logic_in(arg):
    result = arg in supra
    print(result)
    result = arg not in supra
    print(result)


# logic_in('Are'.lower())

# 3. Lab Exercise - operators

def math(fun1, fun2):
    result = fun1 + fun2
    print(result)


# math(10, 15)

def sub(sub1, sub2):
    result = sub1 - sub2
    print(result)


# sub(30, 5)

def multi_div(num1, num2):
    result_multi = num1 * num2
    result_div = num2 / num1
    print(result_multi)
    print(result_div)


# multi_div(5, 5)

# 4. Lab Exercise - Operators


def arg1(sum):
    result_modulus = sum == 20
    print(result_modulus)
    result_modulus = sum % 20
    print(result_modulus)
    result_modulus = sum + 20
    print(result_modulus)
    result_modulus = sum ** 20
    print(result_modulus)


# arg1(20)

