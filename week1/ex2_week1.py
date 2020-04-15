#Find the number of lines in the file, travel_plans2.txt, and assign it to the variable num_lines.

data = open("travel_plans2.txt", "r")
read_data = data.readlines()
num_lines = len(read_data)
print(num_lines)
data.close()