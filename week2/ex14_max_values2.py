"""
Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how many times each character was seen. Then, find the key with the highest value in this dictionary and assign that key to max_value.
"""

product = "iphone and android phones"

lett_d = {}

for char in product:
    if char not in lett_d:
        lett_d[char] = 0
    lett_d[char] += 1

    
key = list(lett_d.keys())
max_value = key[0]

for key in lett_d:#use the key list
   if lett_d[key] > lett_d[max_value]:
       max_value = key

print(max_value)
    
