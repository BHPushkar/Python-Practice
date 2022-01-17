p=int(input("Number of rows want to print \n"))
q=int(input("Enter 0 or 1 \n"))
r=bool(q)
if r==1:

    for i in range(1,p+i):
        for j in range(1,p+i):
            print("*",end="")
else :
    for i in range(1,0,-1):
        for j in range(1,p+i):
            print("*",end="")


