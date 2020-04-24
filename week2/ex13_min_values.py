"""
Create a dictionary called d that keeps track of all the characters in the string placement and notes how many times each character was seen. Then, find the key with the lowest value in this dictionary and assign that key to min_value.
"""
placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."

d= {}

for char in placement:
    if char not in d:
        d[char] = 0
    d[char] += 1
    
key = list(d.keys())
min_value = key[0]

for key in d:
    if d[key] < d[min_value]:
        min_value = key
        
print(min_value)
