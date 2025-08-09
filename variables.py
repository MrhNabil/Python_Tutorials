# Variable = A container for a value (string, integer, float, boolean)
#          A variable behaves as if it was the value it contains

#string
first_name = "nabil" # between "" everything counts as a string
food = "kacchi"
place = "Bandorban"
email = "1234@whatever.com"

print(f"My name is {first_name}") # we are using f here to print the variable
print(f"I love {food}")
print(f"I like to visit {place}")
print(f"My email address is {email}")

#Integer
age = 25
weight = 70
number_of_phone = 1

print(f"My age is {age}")
print(f"My weight is {weight}kg")
print(f"I have {number_of_phone} smartphone")

#Float
cgpa = 3.5
distance = 17.3
price = 9.99

print(f"My cgpa is {cgpa}")
print(f"The distance from my university to home is {distance}km")
print(f"The burger costs ${price}")

# Boolean
is_alien = False
for_sale = False

if is_alien:
    print("Trump is an alien.")    # is_alien = True will print this
else:
    print("Trump is not an alien.")  # is_alien = False will print this  

if for_sale:
    print("Love can be bought with money.")
else:
    print("Love is a hypothesis.")        