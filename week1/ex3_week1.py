#Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt.
data = open("emotion_words2.txt", "r")
data_read = data.read(40)
first_forty = data_read.strip()#remove the spaces and\n
print(first_forty)
data.close()