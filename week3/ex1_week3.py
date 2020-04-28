"""Write a function named total that takes a list of integers as input, and returns the total value of all those integers added together."""
def total(lst):
    tot = 0
    for num in lst:
        tot += num
    return tot

print(total([3,4,5,6,7]))