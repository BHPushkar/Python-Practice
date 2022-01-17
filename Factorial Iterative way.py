# Iterative way to find a factorial :
def factorial(n):
    fact = 1
    for i in range(n):
        fact = fact * (i + 1)
    return fact
n = int(input("Enter the number "))
print("The factorial of ",n," is" ,factorial(n))