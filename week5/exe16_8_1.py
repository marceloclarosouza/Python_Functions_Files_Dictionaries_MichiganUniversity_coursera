"""
You’re going to write a function that takes a string as a parameter and returns a list of the five most frequent characters in the string. Eventually, you will be able to do this sort of problem without a lot of coaching. But we’re going to step you through it as a series of exercises.
First, the function will count the frequencies of all the characters, as we’ve done before, using a dictionary and the accumulator pattern. Then, it will sort the (key, value) pairs. Finally, it will take a slice of the sorted list to get just the top five. That slice will be returned.
Step 1. Suppose you had this list, [8, 7, 6, 6, 4, 4, 3, 1, 0], already sorted, how would you make a list of just the best 5? (Hint: take a slice).
"""

L = [8, 7, 6, 6, 4, 4, 3, 1, 0]
lista = []

for number in range(len(L)):
    if (number < 5):
        lista.append(L[number])
        
print(lista)

"""
Now suppose the list wasn’t sorted yet. How would get those same five elements from this list?
"""

L = [0, 1, 6, 7, 3, 6, 8, 4, 4]
lista = []##creating new list
L.sort(reverse = True)##sort the list

for number in range(5):
    if number < 5:
        lista.append(L[number])
           
print(lista)