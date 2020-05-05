"""
Write a function called stop_at_four that iterates through a list of 
numbers. Using a while loop, append each number to a new list until 
the number 4 appears. The function should return the new list.
"""

def stop_at_four(my_list):
    """function to stop at a specific value"""
    
    new_list = []
    count = 0
    
    while (count < len(my_list)) and (my_list[count] != 4):
        new_list.append(my_list[count])
        count +=1
        
    return new_list

print(stop_at_four([1,2,3,5,6,4]))

