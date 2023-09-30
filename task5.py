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
print('"Hello {', name, '} Your age is', age - 5, 'Years old, Your Address is', address, '."')

# Q4
print(type(name), end=" ")
print(type(str(age)))
print(type(str(street)), end=" ")
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
print('{:*^50}'.format(first_name).rstrip('*'))
print('{:*^50}'.format(first_name))
print('{:*^50}'.format(first_name).lstrip('*'))

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
print(name_two[-2:] == "HD")

# Q18
msg = "I Love Python And Although I Love GSG with Zakaria"
msg_list = list(msg.split())
print('Number of <Love> is: ' + str(msg_list.count('Love')))

msg_by_letter = list(msg)
print('Number of <t> is:' + str(msg.count('t')))

# Q19
msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace('%7', 'Love', 1))

# Q20
def isPalindrome(s):
    return s == s[::-1]

def isSymmetrical(a, b):
    return a == b

my_list = ['ZakZak', "Zakaria", "A war at Tarawa.", "madam"]
first_half = ''
last_half = ''
num = -1
for item in my_list:
    item = str("".join(item.split()).rstrip(".").lower())
    first_half = item[:int(len(item)/2)]
    last_half = item[int(len(item)/2):]
    pal = isPalindrome(item)
    sym = isSymmetrical(first_half, last_half)
    num += 1
    if sym:
        if pal:
            print(my_list[num] + ' is symmetrical, and ' + my_list[num] + ' is a palindrome.')
            print('#' * 50)
        else:
            print(my_list[num] + ' is symmetrical, but ' + my_list[num] + ' is NOT a palindrome.')
            print('#' * 50)
    else:
        if pal:
            print(my_list[num] + ' is not symmetrical, but ' + my_list[num] + ' is a palindrome.')
            print('#' * 50)
        else:
            print(my_list[num] + ' is not symmetrical, and ' + my_list[num] + ' is NOT a palindrome.')
            print('#' * 50)
