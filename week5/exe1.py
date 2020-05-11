"""You will be sorting the following list by each element’s second letter, a to z. Create a function to use when sorting, called second_let. It will take a string as input and return the second letter of that string. Then sort the list, create a variable called sorted_by_second_let and assign the sorted list to it. Do not use lambda."""

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
list_temp = []

def second_let (x):
    #for char in ex_lst:
        #list_temp.append(char[1])       
    sorted_char = sorted(ex_lst[1])
    return sorted_char
    

sorted_by_second_let = (second_let(ex_lst))
print(sorted_by_second_let)