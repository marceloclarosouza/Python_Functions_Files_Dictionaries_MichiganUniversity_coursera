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

"""
Now take a list L and make a dictionary of counts for how often these numbers appear in the list.
"""
L = [0, 1, 6, 7, 3, 6, 8, 4, 4, 6, 1, 6, 6, 5, 4, 4, 3, 35, 4, 11]
dic = {}#creating a dictionary
for number in L:#counting the retetions
    if number not in dic:
        dic[number] = 0
    dic[number] +=1
print(dic)

"""
Now sort the keys (numbers) based on their frequencies
"""
dic_s = sorted(dic.keys(), key = lambda k: dic[k], reverse = True)#sorting the dictionary
for x in dic_s:
    print("{} appears {} times".format(x, dic[x]))
    
"""
Finally, generalize what you’ve done.
Write a function that takes a string instead of a list as a parameter 
and returns a list of the five most frequent characters in the string.
"""
S = "finallygeneralizewhatyouhavedone"

def ordenar_string(S):
    letter = {}
    list1 = []

    for L in S:
        if L not in letter:
            letter[L] = 0
        letter[L] += 1
    #print(letter)

    lista = sorted(letter.keys(), key = lambda k: letter[k], reverse = True)
    i = 0
    for x in lista:
        if i < 5:
            list1.append(x)
        i+=1
    #print("{} appears {} times".format(x, letter[x]))
    return list1

result = ordenar_string(S)
print(result)




