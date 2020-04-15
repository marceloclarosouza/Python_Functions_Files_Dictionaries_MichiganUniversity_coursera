#Using the file school_prompt2.txt, find the number of characters in the file and assign that value to the variable num_char.

data = open("school_promt2.txt", "w")
data_read = data.read()
num_char = len(data_read)
print(num_char)
data.close()