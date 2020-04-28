"""Write two functions, one called addit and one called mult. addit takes one number as an input and adds 5. mult takes one number as an input, and multiplies that input by whatever is returned by addit, and then returns the result. """
def addit (x):
    y = x + 5
    return y

def mult(x):
    y = addit(x)
    z = x*y
    return z

print(mult(int(input("Type a number"))))