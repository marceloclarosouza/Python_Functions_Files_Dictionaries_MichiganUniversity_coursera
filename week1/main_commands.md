open(filename,'r) : open a read file
open(filename,'w'): open writting file

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