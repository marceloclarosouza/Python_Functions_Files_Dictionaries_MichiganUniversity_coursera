"""The pythonic way to consume the results of enumerate, however, is to unpack the tuples while iterating through them, so that the code is easier to understand. """

fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']

for idx, fruit in enumerate(fruits):
    print(idx, fruit)