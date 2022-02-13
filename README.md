# Election Analysis

## Election Audit Overview
For the data provided by the election commission, additional analysis is required to determine:
1. The voter turnout for each county
2. The county with the highest turnout
3. The percentage of votes for each county

The above will be done using several Python's capabilities (version 3.7.6), including, but not limited to:
* import csv
* import os
* read from csv file
* write report in terminal and txt file
* use of "if" and "for" (loop), to count votes for each candidate and county
* use of "list" and "dictionary"

## Election Audit Results
### Total votes cast
In this election, a grand total of 369,711 votes were cast, as shown in the following screenshot:

![Total Votes](Resources\2_1_elec_resul.png")

### Votes per county
The votes for each county are shown hereafter, along with its correspondent percentage.

Denver got the highest turnout with 306,055 votes, equivalent to 82.8% of the total votes.

![Counties](Resources\2_2_counties.png")

### Votes per candidate
As per the candidates, the following screenshot depicts the results of the election, with Diana DeGette getting 272,892 votes, equivalent to 73.8% of the total votes, thus becoming the winner.

![Candidates](Resources\2_3_candid.png")

## Election Audit Summary
The script used in this analysis is "generic", it can be used for any number of counties, any number of candidates, and it will still perform the same analysis.

The results are provided in a **txt file**, which can be read with NotePad (Windows) or TextEdit (Mac).

It is important to keep in mind though, that the source file **"election_results.csv"** had the data as follows:

* Order: ballot number, county name, candidate name
* Separators: commas "," used

If for some reason, the data is ordered differently, the script will be edited to read the data as intended.

If the data separator is not a "comma", this can also be read and interpreted correctly after editing the script.

*We are confident that the analysis, and output provided meets your expectation. We look forward to working with you in future elections. Rest assured that the results are reliable, and will be processed in a timely manner, after performing the required quality data checks.*