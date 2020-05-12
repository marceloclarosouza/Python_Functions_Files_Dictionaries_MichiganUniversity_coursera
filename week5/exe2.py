"""Below, we have provided a list of strings called nums. Write a function called last_char that takes a string as input, and returns only its last character. Use this function to sort the list nums by the last digit of each number, from highest to lowest, and save this as a new list called nums_sorted. """
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

def last_char(x):
    return x[-1]

nums_sorted = sorted(nums, reverse = True, key = last_char)
print(nums_sorted)
