# Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Enter unit (kg, gm, lbs, oz): ")
convert_to = input("Convert into (kg, gm, lbs, oz): ")

if unit == "kg" and convert_to == "gm":
    weight = weight * 1000
    unit = "gm"
    print(f"The weight is {round(weight, 3)} {unit}")
elif unit == "kg" and convert_to == "lbs":
    weight = weight * 2.205
    unit = "lbs"
    print(f"The weight is {round(weight, 3)} {unit}")
elif unit == "kg" and convert_to == "oz":
    weight = weight * 35.274
    unit = "oz"
    print(f"The weight is {round(weight, 3)} {unit}")
elif unit == "gm" and convert_to == "kg":
    weight = weight / 1000
    unit = "kg"
    print(f"The weight is {round(weight, 3)} {unit}")   
elif unit == "gm" and convert_to == "lbs":
    weight = weight * 0.0022
    unit = "lbs"
    print(f"The weight is {round(weight, 3)} {unit}")  
elif unit == "gm" and convert_to == "oz":
    weight = weight * 0.035274
    unit = "oz"
    print(f"The weight is {round(weight, 3)} {unit}") 
elif unit == "lbs" and convert_to == "kg":
    weight = weight / 2.205
    unit = "kg"
    print(f"The weight is {round(weight, 3)} {unit}") 
elif unit == "lbs" and convert_to == "gm":
    weight = weight * 453.592
    unit = "gm"
    print(f"The weight is {round(weight, 3)} {unit}")
elif unit == "lbs" and convert_to == "oz":
    weight = weight * 16
    unit = "oz"
    print(f"The weight is {round(weight, 3)} {unit}")
elif unit == "oz" and convert_to == "kg":
    weight = weight * 0.02835
    unit = "kg"
    print(f"The weight is {round(weight, 3)} {unit}")
elif unit == "oz" and convert_to == "gm":
    weight = weight * 28.3495
    unit = "gm"
    print(f"The weight is {round(weight, 3)} {unit}")
elif unit == "oz" and convert_to == "lbs":
    weight = weight * 0.0625
    unit = "lbs"
    print(f"The weight is {round(weight, 3)} {unit}")
else:
    print(f"{unit} is not valid") 


          