# Dependencies
import os
import csv
from collections import Counter

# Path to collect data from the Resources folder
poll_csv = os.path.join('Resources', 'election_data.csv')

# setting up initial values of variables for calculations
total_votes = 0
candidates_list = []
candidates_dict = {}
percent_votes = 0
highest_vote_rate = 0
winner = ''

# Read in the CSV file
with open(poll_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # capture the header and move to the next row
    header = next(csvreader) 

    # Loop through the rows
    for i, row in enumerate(csvreader):
        
        # Calcualte the total number of votes cast
        total_votes += 1

        # accumulate the list of candidates and votes
        candidates_list.append(row[2])
        

# using the counter method to turn the candidate list to dictionary with candidates as keys and % and number of votes as values
for candidate, votes in Counter(candidates_list).items():
    #calculating percent of votes for the candidate
    percent_votes = round(votes / total_votes * 100, 3)
    candidates_dict[candidate] = [percent_votes, votes]
    # checking whether this is the winning vote
    if percent_votes > highest_vote_rate:
        highest_vote_rate = percent_votes
        winner = candidate

# print to terminal and export results to text file 
"""creating a function that does both the printing and the export """
def out(message):
    print(message)
    with open('analysis\pypoll_output.txt', 'a') as output:
        print(message, file=output)
        
"""using the function to print and export all the required info"""
out('Election Results')
out('-' *50)
out(f'Total Votes: {total_votes:,}')
out('-' *50)
for candidate, value in candidates_dict.items(): #iterating on the new dictionary that includes the percent and nuber of votes as the values
    out(f'{candidate}: {value[0]}% ({value[1]:,})')
out('-' *30)
out(f'Winner: {winner}')
out('-' *50)
