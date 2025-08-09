# Typecasting = the process of converting a variable from one data type to another
#              str(), int(), float(), bool()

name = "Nabil"
age = 25
cgpa = 3.5
gpa = 3.2
is_student = True

print(type(name)) # shows what data type is this variable
print(type(age))
print(type(cgpa))
print(type(is_student))

print(name)
print(age)
print(cgpa)
print(is_student)

name = bool(name) # converting name variable in bool
age = float(age)
cgpa = int(cgpa)
is_student = str(is_student)

print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_student))

print(name) # it will show true as boolean until is a value written between "" , If there is no value it will show false
print(age)
print(cgpa)
print(is_student)
