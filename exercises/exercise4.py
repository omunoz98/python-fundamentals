# 2-8 Number Eight, adding, subtracting, multiplying, and dividing
# Each operation to result in the number eight.
print(5+3)
print(12-4)
print(4*2)
print(16/2)

# 2-9 Favorite Number. Use a variable to represent your favorite number.
# Then, using that variable, create a message that reveals your
# favorite number. Print that message.

fav_number = 10
print(fav_number)

# Assign variables to following sets of numbers. Use underscores to make them more readable.
# Write a function called number_sets and print each variable inside the function.
# Call all the function to verify your results.
# a.456234 b.68423791 c.13794628 d.96374

number_a = '456_234'
number_sets = number_a
print(number_sets)

number_b = '68_423_791'
number_sets = number_b
print(number_sets)

number_c = '13_794_628'
number_sets = number_c
print(number_sets)

number_d = '96_374'
number_sets = number_d
print(number_sets)

# Write a function that will take 2 arguments.
# Using Type conversion, convert the first argument from int to float.
# Convert the second argument from float to int.
# Call the function and provide the correct values for each argument to verify your results.
# One argument should be a float and the other an int

def num(arg1, arg2):
    print(arg1)
    print(arg2)

arg1 = 10
arg2 = 10.5

num(arg1, arg2)

arg1 = float(10.5)
arg2 = int(10)
print(num(arg1, arg2))

# Write a function that will have two inputs.
# The first input method should ask “What is your favorite movie”
# the second input method should ask “How many times have you seen it?”.
# The second input should be inside an int function. Each input method should be assigned to a variable.
# In a print statement using placeholders,
# the output result should be “I have seen {favorite movie} {number of times} times”

fun = input("What is your favorite movie?")
fun2 = input("How many times have you seen it?")
print(fun)

output = "I have seen {0} {1} times"
print(output.format(fun, fun2))
