# Data needed:

# Total number of votes cast
# Names of all the candidates
# Percentage of votes each candidate won
# Total numbrer of votes for each candidate
# Winner based on popular vote

# Add our dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("C:\\Users\\luisp\\Desktop\\Election_Analysis\\Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("C:\\Users\\luisp\\Desktop\\Election_Analysis\\Analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []

# Declare the empty dictionary.
candidate_votes = {}

# Open the election results and read the file
with open(file_to_load) as election_data:

#   print(election_data)
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    print(headers)

# Print each row in the CSV file
    for row in file_reader:
                
        # Add to the total vote count.
        total_votes += 1
        
    # Print the candidate name from each row.
        candidate_name = row[2]
    
    # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
    
    # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            
    # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
    # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Print the candidate list.
print(candidate_votes)
        

# Print the total votes
print(f"Total votes = ", total_votes)
