"""Write a function called count that takes a list of numbers as input and returns a count of the number of elements in the list."""
def count(lst):
    tot = 0
    for i in (lst):
        tot += 1
    return tot

print(count([1,2,3,4,5,6,7,7]))