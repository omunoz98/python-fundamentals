# 10-6 & 10-7 Addition
# print('enter two numbers to add both numbers')
# print("enter 's' to stop execution.")

while True:
    num1 = input("enter first number: ")
    if num1 == 's':
        break
    num2 = input("enter second number: ")
    if num2 == 's':
        break

    try:
        result = int(num1) + int(num2)
        #print(f"the result is {result}")
    except ValueError:
        print('Wrong value was provided. Enter two numbers!')

#10-8 & 10-9 Cats and dogs

file1 = 'cats.txt'
file2 = 'dogs.txt'

print('Cats: ')
try:
    with open(file1) as f:
        stuff = f.read()
except FileNotFoundError:
    print(f'Cannot find, {file1} sorry try again.')
    pass
else:
    print(stuff)
print("dogs: ")
try:
    with open(file2) as f:
        stuff = f.read()
except FileNotFoundError:
    print(f"Cannot find, {file2} sorry try again.")
    pass
else:
    print(stuff)

