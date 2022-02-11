import os

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("C:\\Users\\luisp\\Desktop\\Election_Analysis\\Analysis", "txt_file.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello World!!!")
    
    # Write three counties to the file.
    txt_file.write("Arapahoe, ")
    txt_file.write("Denver, ")
    txt_file.write("Jefferson")
    txt_file.write("\n--------")
    
    # Write three counties to the file.
    txt_file.write("\nArapahoe\nDenver\nJefferson")