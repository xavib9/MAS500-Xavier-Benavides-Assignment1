# Print out all the state names from the csv
# Coded in the "imperative" style

f = open('2012_US_election_state.csv', 'r')
print "Opened file:"

all_lines = f.readlines()
obama = 0 
romney = 0
for line in all_lines:
    columns = line.split(",")
   	#Check if the string is a number
    if columns[3].isdigit():
    	#If it is a number we need to accumulate this value in Obama's votes
    	#Convert string to integer in order to accumulate the value
    	obama = obama + int(columns[3])

    #Check if the string is a number
    if columns[5].isdigit():
    	#If it is a number we need to accumulate this value in Romney's votes
    	#Convert string to integer in order to accumulate the value
    	romney = romney + int(columns[5])


#Print the final value / Convert integer to String.
print "Votes for Obama: " + str(obama)
print "Votes for Romney: " + str(romney)
