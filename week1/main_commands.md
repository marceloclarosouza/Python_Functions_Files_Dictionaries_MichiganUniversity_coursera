open(filename,'r) : open a read file
open(filename,'w'): open writting file

open("../myData/data2.txt", "r")

filevariable.close() : file use is complete
filevar.write("astring") : Add a string to the end of the file
filevar.read(): Read and return a string of n characters, or the entire file as a single string if n is not provided.

filevar.readline() :Read and return the next line of the file with all text up to and including the newline character.

filevar.readlines() :Returns a list of strings, each representing a single line of the file.

fileref = open("olympics.txt", "w")
lines = fileref.readlines()#to select the lines
for lin in fileref:#print all lines
    print(lin.strip())# strip remove spaces and \n at the end of the line
fileref.close()


Examples:
#Using the file school_prompt2.txt, find the number of characters in the file and assign that value to the variable num_char.
data = open("school_promt2.txt", "w")
data_read = data.read()
num_char = len(data_read)
print(num_char)
data.close()

#Find the number of lines in the file, travel_plans2.txt, and assign it to the variable num_lines.
data = open("travel_plans2.txt", "r")
read_data = data.readlines()
num_lines = len(read_data)
print(num_lines)
data.close()

#Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt.
data = open("emotion_words2.txt", "r")
data_read = data.read(40)
first_forty = data_read.strip()#remove the spaces and\n
print(first_forty)
data.close()

#To process all of our olypmics data, we will use a for loop to iterate over the lines of the file. Using the split method, we can break each line into a list containing all the fields of interest about the athlete. We can then take the values corresponding to name, team and event to construct a simple sentence.

olympicsfile = open("olympics.txt", "r")
for aline in olympicsfilr.readlines():  #### or use "for aline in alympcsfile:" (pythonning best writting)
    values = aline.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])
olympicsfile.close()


#Write code to find out how many lines are in the file emotion_words.txt as shown above. Save this value to the variable num_lines. Do not use the len method.
data = open("emotion_words.txt", "r")
num_lines = 0

for lim in data.readlines():
    num_lines += 1

print(num_lines)

Examples of reading and writting files:

fule = "squared_numbers.txt"
outfile = open(filenames, "w")

for number in range(1,13):
    square = number * number
    outfile.write(str(square)+ "\n")

outfile.close()

infile = open(filename, "r")
print(infile.read()[:10])
infile.close()

