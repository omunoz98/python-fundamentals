# Lesson 6 - Control Flow Statements

# Boolean
# These values are either True or False

def boolen_sample():
    print(bool('sample'))
    print(bool(0.0))


# boolen_sample()

# If Statement example.
# used to fins out if a condition is true
def basic_if(arg1, arg2):
    if arg1 > arg2:
        print('argument1 is greater than argument2')

    if arg1 == arg2:
        print('both values are the same')


# basic_if(10, 5)


# elif example
# used when the first condition is false and you to try another
def basic_if_elif(arg):
    if(arg > 10):
        print('sum is greater than 10')
    elif arg == 10:
        print('sum is 10')
    elif arg < 10:
        print('sum is less than 10')

# basic_if_elif(10)



# else statement
# This keyword can be used to execute a block of code when the IF statement
# results are false
def else_example(arg):
    if arg > 15:
        print('are argument is greater than 15')
    else:
        print('Our argument is less than 15')


# else_example(12)


# else with elif
def check_grade(arg):
    if arg == 'A':
        print('Excellent')
    elif arg == 'B':
        print('Good')
    elif arg == 'C':
        print ('Average')
    elif arg == 'D':
        print('Below Average')
    elif arg == 'F':
        print('Failed')
    else:
        print('Grade not valid')


# check_grade('Dro')

# nested IF statement
# This allows an if statement to be inside another if statement.
# The inner if statement only evaluates if the outer if is true.
happy = 14


def nested_example(arg):
    if happy > arg:
        print('happy is greater than argument')
        if arg > 5:
            print('argument is greater than 5')
        else:
            print('argument is less than 5')


# nested_example(4)

# Ternary Statement
# One condition can be performed on one line
# Basically a shorthand if statement
golf = 22
hotel = 24

# if shorthand
result = golf if golf > hotel else hotel
print(result)

print('both are equal' if golf == hotel else 'golf is greater' if golf
      > hotel else 'hotel is greater')


# this function will break down the above shorthand if
def if_short_decoded():
    if golf == hotel:
        print('both are equal')
    elif golf > hotel:
        print('golf is greater')
    else:
        print('hotel is greater')


# if_short_decoded()


# and & or keyword
def combined(arg1, arg2, arg3):
    if arg1 > arg2 and arg1 >= arg3:
        print('argument 1 is the greatest')

    if arg2 > arg3 or arg2 <= arg3:
        print('argument 2 is less or equal to 3 but not 1')


combined(30, 20, 30)
