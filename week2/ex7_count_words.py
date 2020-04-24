"""
Provided is a string saved to the variable name sentence. Split the string into a list of words, then create a dictionary that contains each word and the number of times it occurs. Save this dictionary to the variable name word_counts
"""

sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
words = sentence.split()
print(words)

word_counts = {}
for counts in words:
    if counts not in word_counts:
        word_counts[counts]=0
    word_counts[counts] += 1
    
for counts in word_counts.keys():
    print(counts + " " + str(word_counts[counts]))
    