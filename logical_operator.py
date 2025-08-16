# logical operator help us to evaluate multiple conditions (or, and, not)
#       or  = at least one condition must be true
#       and = both conditions must be true
#       not = inverts the condition
'''
temp = 25
is_raining = False

if temp == 25 and is_raining:
    print("Program is canceled!")
else:
    print("Let's go!!")
'''

'''
temp = float(input("Enter the temperature: "))
is_raining = False


if temp > 35 or temp < 0 or is_raining:
    print("Program is canceled!")
else:
    print("Have to go!")
'''

temp = float(input("Enter the temperature: "))
is_raining = input("Is it raining? (yes/no): ").lower() == "yes"

if temp > 35 or temp < 0 and is_raining:
    print("Program is canceled!")
else:
    print("Have to go!")








