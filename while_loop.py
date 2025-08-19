# while loop = execute some code WHILE some codes remains true

#name = input("Enter your name: ")
#age = int(input("Enter your age: "))
#food = input("Enter a food you like (q to quit): ")
num = int(input("Enter a number # between 1 - 10: "))

'''
while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ") # in while loop if the if the 1st codition is not fullfilled the loop will continue to print this line. If there is no such line like this you will stuck in a infinite loop

print(f"Hello {name}")                # This is the exit loop
'''
"""
while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old") 
"""
'''
while not food == "q":
    print(f"You are {food}")
    food = input("Enter a another food you like (q to quit): ") 

print("bye")
'''

while num < 1 or num > 10:
    print(f"{num} is not a valid input (Hint: 1 - 10)")
    num = int(input("Enter a number # between 1 - 10: "))

print(f"Your number is {num}")
