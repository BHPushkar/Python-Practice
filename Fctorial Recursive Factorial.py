print("Enter a number")
n=int(input())
def factorial_recursive(n):
    if n==1 :
        return 1
    else :
        return n*factorial_recursive(n-1)       # It will go for n and first will give n*(n-1)*factorial_recursive(n-2
print("The factorial by recursive method is ",factorial_recursive(n))


