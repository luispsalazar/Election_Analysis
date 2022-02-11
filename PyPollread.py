# Assign a variable for the file to load and the path
file_to_load = "C:\\Users\\luisp\\Desktop\\Election_Analysis\\Resources\\election_results.csv"


# Open the election results and read the file
election_data = open(file_to_load, 'r')

# To do: perform analysis
print(election_data)

# Close the file
election_data.close()
