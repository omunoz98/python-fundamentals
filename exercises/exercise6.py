# 1 Do it yourself, 5-3.


def colors(alien):
    if alien == 'green':
      print('Green alien earned 5 points')
    elif alien == 'yellow':
        print('yellow alien has no points')
    elif alien == 'red':
        print('red alien has no points')

# colors('green')

def color(alien):
    if alien == 'green':
        print('Green alien earned 5 points')
    if alien == 'yellow':
        print('Yellow alien has no points')
    if alien == 'Red':
        print('Red alien has no points')

# color('green, yellow')


# 5-4 do it yourself

def alien_colors(aliens):
    if aliens == 'green':
        print('Green alien earned 5 points')
    else:
        print('Red alien earned 10 points')
        print('yellow alien earned 10 points')

# alien_colors(10)

# 5-5 Do it yourself


def alien_colors3(alien):
    if alien == 'green':
        print('Green alien earned 5 points')
    elif alien == 'yellow':
        print('yellow has earned 10 points')
    else:
        print('red alien has earned 15 points')

# alien_colors3(15)

# 5-6 Do it yourself. Page 85.

# age = 2


def stages_of_life(age):
    if age <= 2:
        print('age is 2 or less they are a baby')
    elif age <= 4:
        print('age is less than 4 but at least 2 they are a toddler')
    elif age <= 13:
        print('age is less than 13, but at least 4 they are a kid')
    elif age <= 20:
        print('at least 13 but less than 20 they are a teen')
    elif age <= 65:
        print('at least 20 but less than 65 they are an adult')
    else:
        print('65 or older, they are an elder')


# stages_of_life(75)

# Lab Exercise Q5.

def boolean_example(number):
    if number < 5:
        print('number is less than 5')
        print(bool('example'))
        print(bool(4))

# boolean_example(4)

