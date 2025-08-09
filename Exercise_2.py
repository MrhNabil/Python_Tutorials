# Exercise_2 Shopping cart
item = input("What item would you like to buy?: ")
price = float(input("Price of the item : "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} X {item}'s")
print(f"Your total bill is {total} taka.")