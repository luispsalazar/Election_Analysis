# Data needed:
# 1 Total number of votes cast
# 2 Names of all the candidates
# 3 Percentage of votes each candidate won
# 4 Total numbrer of votes for each candidate
# 5 Winner based on popular vote

# Add our dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("C:\\Users\\luisp\\Desktop\\Election_Analysis\\Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("C:\\Users\\luisp\\Desktop\\Election_Analysis\\Analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
#    print(election_data)
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    print(headers)

# Print each row in the CSV file
    for row in file_reader:
        #print(row)
        
        # 2. Add to the total vote count.
        total_votes += 1

# 3. Print the total votes
    print(f"Total votes = ", total_votes)
