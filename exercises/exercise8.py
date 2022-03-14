# 5-8 and 5-9 Try it yourself
# 5-8 Hello Admin:

staff = ['jaden', 'john', 'peter', 'alex', 'admin']


def staff_admin():
    if 'admin' in staff:
        print('hello admin would you like to see a status report?')
    else:
        print('hello, [] thank you for logging in again'.format(staff))


# staff_admin()

# 5-9:


def hello_admin():
    if len(staff) == 0:
        print('we need to find more users!')
    else:
        for person in staff:
            if staff == "admin":
                print("hello admin, would you like to see status report?")
            else:
                print("Hello, {} welcome back!".format(person))

# hello_admin()
# 5-10

current_users = ['user1', 'user2', 'user3', 'user4', 'user5']
new_users = ['user1', 'user6', 'user7', 'user8', 'user9']

def new_user():
    for user1 in new_users:
        print(user1)
    else:
        print('user1 enter new username.')

# new_user()

# 5-11

ord_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def ordinal():
    for ord in ord_list:
        if ord == 1:
            print('{}st'.format(ord))
        elif ord == 2:
            print('{}nd'.format(ord))
        elif ord == 3:
            print('{}rd'.format(ord))
        else:
            print('{}th'.format(ord))

# ordinal()

# 6-1 Try it yourself

persons = {'first_name': 'omar', 'last_name': 'munoz', 'age': 23, 'city': 'wichita'}
print(persons['first_name'])
print(persons['last_name'])
print(persons['age'])
print(persons['city'])

# 6-7 Try it yourself

people = {
    persons:{
        'first_name': 'omar', 'last': 'munoz', 'age': 23, 'city': 'wichita',
        'first_name1': 'alyson', 'last_name1': 'dominguez', 'age1': 13,
        'first_name2': 'heidy', 'last_name2': 'ochoa', 'age2': 20,
    },
}


for people, persons in persons.items():
    print(persons)





