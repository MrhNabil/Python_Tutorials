# if = Do some code only if the condition is True
#      Else do something else

age = int(input("Enter your age: "))

if 100 > age >= 18:
    print("You are eligible for credit card!")
elif age >= 100:
    print("You don't a credit card, you need to rest")
elif age < 0:
    print("You need to born in the earth first!")        
else:
    print(f"You need to wait for {18-(age)} years")    