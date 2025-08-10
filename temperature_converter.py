
temp = float(input("Enter the temperature :"))
unit = input("Is the temperature in Celsius or Fahrenheit (C/F): ")

if unit == "C":
    temp = round((temp * 9/5) + 32, 2)
    print(f"The temperature in Fahrenheit {temp}°F")  # alt + 0176 = °
elif unit == "F":
    temp = round((temp - 32) * 5/9, 2)
    print(f"The temperature in Celsius {temp}°C")  # alt + 0176 = °
else:
    print(f"{unit} is not valid")
