# Import the datetime class from the datetime module

#import datetime as dt
#from ensurepip import version
# Use the now() attribute on the datetime class to get the present time
#now = dt.datetime.now()
# Print the present time
#print("The time right now is ", now)



# Data needed:
# 1 Total number of votes cast
# 2 Names of all the candidates
# 3 Percentage of votes each candidate won
# 4 Total numbrer of votes for each candidate
# 5 Winner based on popular vote


#import csv

#with open('\Users\luisp\Desktop\Election_Analysis\Resources\election_results.csv', 'r') as election_data:
#    csv_reader = csv.reader(election_data)

#    next(csv_reader)

#    for line in csv_reader:
#        print(line)


# Assign a variable for the file to load and the path
#file_to_load = 'Resources\election_results.csv'

# Open the election results and read the file
#election_data = open(file_to_load, 'r')

# To do: perform analysis

# Close the file
#election_data.close()


#import csv
#import os

# Assign a variable for the file to load and the path

#file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file

#with open(file_to_load) as election_data:

# Print the file object

#     print(election_data)





# Add our dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

# 3. Print the total votes
print(total_votes)