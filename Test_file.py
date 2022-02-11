import os

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("C:\\Users\\luisp\\Desktop\\Election_Analysis\\Analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")

# Write some data to the file.
outfile.write("Hello World!!")

# Close the file
outfile.close()