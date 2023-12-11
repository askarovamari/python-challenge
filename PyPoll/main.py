# Import os & csv modules
import os
import csv

# open and read csv
csvpath = os.path.join('Resources','election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    # Declare starting variables (blank lists)
    Votes = []
    County = []
    Candidates = []
    Charles_Casper_Stockham = []
    Diana_DeGette = []
    Raymon_Anthony_Doane = []
    Charles_Casper_Stockham_votes = 0
    Diana_DeGette_votes = 0
    Raymon_Anthony_Doane_votes = 0

    # Read throough each line of the dataset
    for row in csvreader:
        Votes.append(int(row[0]))
        County.append(row[1])
        Candidates.append(row[2])

    # Count total number of votes
    total_votes = (len(Votes))
    

    # Votes per Candidate
    for candidate in Candidates:
        if candidate == "Charles Casper Stockham":
            Charles_Casper_Stockham.append(Candidates)
            Charles_Casper_Stockham_votes = len(Charles_Casper_Stockham)
            
        elif candidate == "Diana DeGette":
            Diana_DeGette.append(Candidates)
            Diana_DeGette_votes = len(Diana_DeGette)
            
        else:
            Raymon_Anthony_Doane.append(Candidates)
            Raymon_Anthony_Doane_votes = len(Raymon_Anthony_Doane)
    
    
    # Percentage of votes per Candidate
    Charles_Casper_Stockham_prcnt = round(((Charles_Casper_Stockham_votes / total_votes) * 100), 3)
    Diana_DeGette_prcnt = round(((Diana_DeGette_votes / total_votes) * 100), 3)
    Raymon_Anthony_Doane_prcnt = round(((Raymon_Anthony_Doane_votes / total_votes) * 100), 3)

    
    # Declare a winner
    if Charles_Casper_Stockham_prcnt > max(Diana_DeGette_prcnt, Raymon_Anthony_Doane_prcnt):
        winner = "Charles_Casper_Stockham"
    elif Diana_DeGette_prcnt > max(Charles_Casper_Stockham_prcnt, Raymon_Anthony_Doane_prcnt):
        winner = "Diana_DeGette"  
    else:
        winner = "Raymon_Anthony_Doane"


    # Print Statements
    print(f'''Election Results
-----------------------------------
Total Votes: {total_votes}
-----------------------------------
Charles Casper Stockham: {Charles_Casper_Stockham_prcnt}% ({Charles_Casper_Stockham_votes})
Diana DeGette: {Diana_DeGette_prcnt}% ({Diana_DeGette_votes})
Raymon Anthony Doane: {Raymon_Anthony_Doane_prcnt}% ({Raymon_Anthony_Doane_votes})
-----------------------------------
Winner: {winner}
-----------------------------------''')

# Write a txt file

output_path = os.path.join("Analysis", "analysis.txt")
with open(output_path, 'w') as text:
    text.write(f'''Election Results
-----------------------------------
Total Votes: {total_votes}
-----------------------------------
Charles Casper Stockham: {Charles_Casper_Stockham_prcnt}% ({Charles_Casper_Stockham_votes})
Diana DeGette: {Diana_DeGette_prcnt}% ({Diana_DeGette_votes})
Raymon Anthony Doane: {Raymon_Anthony_Doane_prcnt}% ({Raymon_Anthony_Doane_votes})
-----------------------------------
Winner: {winner}
-----------------------------------''')