# conditional expression = A one line shortcut for if-else statement (ternary operator)
#                          print or assign oone of two values based on condition
#                          X if condition else Y

num = 61
a = 6
b = 7
age = 25
temperature = 36
user_role = input("You are (admin or guest): ")

#print("Positive" if num > 0 else "Negative")
#print("Passed" if num >= 60 else "You dumb... You failed!!")

#result = "Even" if num % 2 == 0 else "ODD"

#max_num = a if a > b else b
#min_num = a if a < b else b

#status = "Not Married" if age <= 25 else "You are too old to get married!"
#weather = "Too Hot 🥵" if temperature > 35 else "Normal 😐"

access_level = "Full Access" if user_role == "admin" else "You will get, what you have paid for!"

print(access_level) 
