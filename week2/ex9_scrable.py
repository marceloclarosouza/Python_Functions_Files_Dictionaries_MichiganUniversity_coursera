"""
 suppose that we wanted to compute a Scrabble score for the Study in Scarlet text. Each occurrence of the letter ‘e’ earns one point, but ‘q’ earns 10. We have a second dictionary, stored in the variable letter_values. Now, to compute the total score, we start an accumulator at 0 and go through each of the letters in the counts dictionary. For each of those letters that has a letter value (no points for spaces, punctuation, capital letters, etc.), we add to the total score
"""

f = open("scarlet.txt", "r")
txt = f.read()#txt is along list of char
x = {}#strat an empty dictionary
for c in txt:
    if c not in x:
        x[c] = 0
        
    x[c] += 1
    

#start the scrabble game
    
letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f':4, 'g': 2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}


tot = 0
for y in x:# "x" is the library
    if y in letter_values:# letter_values is a dcitionary
        tot += letter_values[y]*x[y]# multiply the y score with x cores. Key values of both lists
        
print(tot)
        