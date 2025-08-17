# validate user input exercise
# usename is not more than 12 characters
# username must not contain spaces
# username must not contain digits

user_name = input("Enter your name: ")

if len(user_name) > 12 :
    print("your username can't be nore than 12 characters!")
elif not user_name.find(" ") == -1:
    print("Your username can't contain spaces")
#elif user_name.isalpha() == False :
#    print("Your username must not contain any digits.")
elif not user_name.isalpha():
    print("Your username can't contain any digits.")
else:
    print(f"Welcome {user_name}")