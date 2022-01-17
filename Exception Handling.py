print("Enter first number ")
p=input()
print("Enter second number ")
q=input()
try:
    print("The sum is ",a+b)

except Exception as e:                       # the "E" is capital
    print(e)


print("This line must get printed ")           # Here to print this line , evenif some error found
                                                   # in above code try and except is used
