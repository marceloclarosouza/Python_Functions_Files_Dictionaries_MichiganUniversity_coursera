#Create a list called destination using the data stored in travel_plans.txt. Each element of the list should contain a line from the file that lists a country and cities inside that country. Hint: each line that has this information also has a colon : in it.

travel_plans.txt 
This summer I will be travelling.
I will go to...
Italy: Rome
Greece: Athens
England: London, Manchester
France: Paris, Nice, Lyon
Spain: Madrid, Barcelona, Granada
Austria: Vienna
I will probably not even want to come back!
However, I wonder how I will get by with all the different languages.
I only know English!


travel = open("travel_plans.txt", "r")
lines = travel.readlines()
destination = []

for dest in travel:
    if ":" in dest:
        destination.append(dest)
print(destination)
travel.close()