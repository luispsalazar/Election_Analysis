import csv

# Create a filename variable to a direct or indirect path to the file
with open("analysis", "election_analysis.txt", newline = '') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')

    for row in rows:
        print(row)

