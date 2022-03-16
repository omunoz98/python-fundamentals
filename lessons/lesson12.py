# lesson 12 exception handling

def sample_divide():
    print('let\'s divide two numbers.')
    try:
        first = input('the first number is?')
        second = input('the second number is?')
        answer = int(first) / int(second)
        print(answer)
    except (ZeroDivisionError, ValueError):
        print('You can\'t divide by zero or use strings')


# sample_divide()

def multi_except_sample():
    names = ('Dave', 'Matt', 'Jody')
    these = (25.4, '30j', 34)

    try:
        delta = int(these[3])
        echo = complex(these[0], 5)
        print('Delta is '+ str(delta))
    except IndexError:
        print('Please provide at least 1 argument')
    except ValueError:
        print('That is not a number')
    except TypeError:
        print('You have provided something weird')
    except NameError:
        print('I don\'t know how to calculate that.')

# multi_except_sample()

# the else block can be used to be execute code that does not need to be tested.
# this else will only execute if the try succeeds
alpha, fox = 5, 10

def sample_except_else(arg):
    try:
        if fox > arg:
            golf = fox / arg
            print('value is {0}'.format(golf))
    except ZeroDivisionError:
        print('Error has occurred')
    else:
        print('division was successful')

# sample_except_else(2)

# the finally block is executed regardless of whether the try block succeeds
def sample_finally():
    try:
        if fox > alpha:
            bravo = fox / (fox - alpha) - 5
            charile = fox / 0
            print('Value is {0}'.format(bravo))

    except ZeroDivisionError:
        print('Error has occurred')
    else:
        print('else prints')
    finally:
        print('finally prints')


sample_finally()
