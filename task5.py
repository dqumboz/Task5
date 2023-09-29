# Q1
name = str(input('Write your name here\n'))
age = int(input('Enter your age here\n'))
street = int(input('Enter the street where are you live\n'))
city = str(input('Enter the city where are you live\n'))
country = str(input('Enter the country where are you live\n'))

# Q2
address = f'{street}, {city}, {country}'
all_data = f'''"Name: {name}"
"Age: {age}"
"Address: {address}"'''
print(all_data)

# Q3
print(f'"Hello {name} Your age is {age - 5} Years old, Your Address is {address}."')

print('Hello {', name, '} Your age is', age - 5, 'Years old, Your Address is', address)

# Q4
print(type(name), end=" ")
print(type(age))
print(type(street), end=" ")
print(type(city))
print(type(country))

# Q5
par = f'''"Hello {name}, How are you? \ """ your Age is "{age - 5}"" + And your Country Is: {country}'''
print(par.title())

# Q6
par = f'''"Hello {name}, How are you? \ 
""" your Age is "{age - 5}"" + And
your Country Is: {country}'''
print(par)

# Q7
name = 'ITF Gsg Python'
print('First Letter Is "' + name[0] + '"')
print('Third Letter Is "' + name[2] + '"\n')
print('Last Letter Is "' + name[-1] + '"')

# Q8
print(name[-3:])
print(name[:3])
print()
print(name[:7:2])
print()
print(name[-1:7:-1])

# Q9
name = "$&$&Mohammed$&$&"
print(name.strip("$&"))

# Q10
msg = 'I %7 Python And Although I %7 GSG with Zakaria'
print(msg.replace("%7", "Love"))

# Q11
num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = "87190"

print(num1.zfill(5))
print(num2.zfill(5))
print(num3.zfill(5))
print(num4.zfill(5))
print(num5.zfill(5))
print(num6.zfill(5))

# Q13
txt = 'dema qumboz'
# that make the first letter in first word is capital
print(txt.capitalize())
# that make the first letter in every word is capital
print(txt.title())

# Q14
first_name = "Dema"

# Q15
name_one = "SaMER"
name_two = "Abed"
print(name_one.swapcase())
print(name_two.swapcase())
print(name_one.lower())
print(name_two.upper())

# Q16
print(name_one.isupper())
print(name_two.islower())

# Q17
print(name_one[0] == "S")
print(name_two[2:] == "ed")

# Q18
msg = "I Love Python And Although I Love GSG with Zakaria"
msg_list = list(msg.split())
print('Number of <Love> is: ' + str(msg_list.count('Love')))

msg_by_letter = list(msg)
print('Number of <t> is:' + str(msg.count('t')))

# Q19
msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace('%7', 'Love', 1))

# Q20 متاكدة اله حل اسهل من هيك هافكر فيه و اعدل
test1 = "ZakZak"
test2 = "Zakaria"
test3 = "A war at Tarawa.".lower()
test4 = "madam"

test3_rep = test3.replace(" ", "")
test3_rep = test3_rep.replace('.', '')

half = int(len(test1)/2)
first_str = test1[:half]
last_str = test1[half:]

if first_str == last_str:
    if test1 == test1[::-1]:
        print(test1 + ' is symmetrical, but ' + test1 + ' is a palindrome.')
    else:
        print(test1 + ' is symmetrical, but ' + test1 + ' is NOT a palindrome.')
else:
    if test1 == test1[::-1]:
        print(test1 + ' is NOT symmetrical, and ' + test1 + ' is a palindrome.')
    else:
        print(test1 + ' is NOT symmetrical, and ' + test1 + ' is NOT a palindrome.')

half = int(len(test2)/2)
first_str = test2[:half]
last_str = test2[half:]

if first_str == last_str:
    if test2 == test2[::-1]:
        print(test2 + ' is symmetrical, but ' + test2 + ' is a palindrome.')
    else:
        print(test2 + ' is symmetrical, but ' + test2 + ' is NOT a palindrome.')
else:
    if test2 == test2[::-1]:
        print(test2 + ' is NOT symmetrical, and ' + test2 + ' is a palindrome.')
    else:
        print(test2 + ' is NOT symmetrical, and ' + test2 + ' is NOT a palindrome.')

half = int(len(test3_rep)/2)
first_str = test3_rep[:half]
last_str = test3_rep[half:]

if first_str == last_str:
    if test3_rep == test3_rep[::-1]:
        print(test3 + ' is symmetrical, but ' + test3 + ' is a palindrome.')
    else:
        print(test3 + ' is symmetrical, but ' + test3 + ' is NOT a palindrome.')
else:
    if test3_rep == test3_rep[::-1]:
        print(test3 + ' is NOT symmetrical, and ' + test3 + ' is a palindrome.')
    else:
        print(test3 + ' is NOT symmetrical, and ' + test3 + ' is NOT a palindrome.')

half = int(len(test4)/2)
first_str = test4[:half]
last_str = test4[half:]

if first_str == last_str:
    if test4 == test4[::-1]:
        print(test4 + ' is symmetrical, but ' + test4 + ' is a palindrome.')
    else:
        print(test4 + ' is symmetrical, but ' + test4 + ' is NOT a palindrome.')
else:
    if test4 == test4[::-1]:
        print(test4 + ' is NOT symmetrical, and ' + test4 + ' is a palindrome.')
    else:
        print(test4 + ' is NOT symmetrical, and ' + test4 + ' is NOT a palindrome.')
