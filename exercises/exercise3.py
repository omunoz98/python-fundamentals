# For this lab exercise create a file called exercise3.py.
# Once you have completed your work
# be sure to check your code into your local repository and push your changes to GitHub.
# Once completed you will need to log into your GitHub account
# and get a direct link to your exercise3.py file in order to turn this exercise in.
# That URL should be part of your response for this task.
# On page 25 of your book, In the Try it Yourself section do the following tasks.
# Put all your code in your exercise3.py file.
# 2-3 Personal Message
# 2-4 Name Cases
# 2-5 Famous Quotes
# 2-6 Famous Quotes
# 2-7 String Names

# 2-3 Personal Message
message_to_eric = '''Hello Eric, would you like to learn some Python today?'''
print(message_to_eric)

# 2-4 Name Cases
first_name = "omar"
last_name = "munoz"
full_name = f"{first_name} {last_name}"
print(f"{full_name.title()}")

name = "omar munoz"
print(name.upper())
print(name.lower())

#2-5 Famous Quote

famous_quote = 'Lionel Messi said, "The best decisions aren\'t made with your mind, but with your instinct."'
print(famous_quote)

#2-6 Famous Quote

famous_person = "Lionel Messi"
message = '"The best decisions are\'t made with your mind, but with your instinct."'
print(famous_person, message)

#2-7 Stripping names

name = "\tomar munoz\n"
print(name)

# strip()
print(name.strip())

# lower()
print(name.lower())

# replace()
print(name.replace('e', 'a'))




