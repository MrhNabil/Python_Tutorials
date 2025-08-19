# formate specifier = {value:flags} formate a value based on what flags are inserted

# .(number)f = round to that many decimal spaces (fixed point)
# :(number)  = allocate that many spaces
# :03        = allocate and zero pad that many spaces
# :<         = left justify
# :>         = right justify
# :^         = conter align
# :+         = Use a plus sign to indicate postive value
# :=         = place sign to left most position
# :(space)   = insert a space before positive numbers
# :,         = comma separator

price1 = 344444.14159
price2 = -987444.65444
price3 = 124444.343333

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")

