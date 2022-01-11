
def addition(a,b):
    """This first line in the function is called as docstring and used to know the functions type """

    print("The addition of two numbers is ",a+b)
addition(2,4)
addition(4,6)
addition(8,8)                       # no need to assign variabels indivisually
                                    #none comes in output as no return statement is used

print(addition.__doc__)            # Look now there is dockstring in the output
