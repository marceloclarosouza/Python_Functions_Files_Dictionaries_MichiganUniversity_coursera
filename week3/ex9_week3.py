"""The Pythonic Way to Enumerate Items in a Sequence """
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']

for item in enumerate(fruits):
    print(item[0], item[1])