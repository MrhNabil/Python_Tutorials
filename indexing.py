#indexing = accessing elemnets of a sequence using [] (indexing sequence)
#           [start : end : step]

number = "012-3456789"
credit_number = "1234-3455-0934-0193"
last_digits = credit_number[-4:]
credit_number = credit_number[::-1]   # it will reverse the credit_number

#print(number[3])          # showing which number is present at that index
#print(number[:4])
#print(number[7:11])
#print(len(number))
#print(number[4:])
#print(number[-1])         # -1 print the last number, -2 prints 2nd last and -3.... so on
#print(number[::2])        # in step [::2] is print every 2nd character and so on

#print(f"XXXX-XXXX-XXXX-{last_digits}")
print(credit_number)

