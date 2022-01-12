p=input("Enter a number ")
p=int(p)
while (True):

    if p>100:
         print("Entered number is greater than 100")
         break                         #break used to end the loop after required result
    if p<100:
         print("Try again")
         break
