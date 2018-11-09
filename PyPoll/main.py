import os
import csv

csvfile = os.path.join('election_data.csv')
with open(csvfile) as csvfile:
    readcsv = csv.reader(csvfile, delimiter=',')
    print(readcsv)
    header = next(readcsv)
    print(header)



    vote_count = 0
    candidates = {}
    percentage_votes = {}
    winner = ""
    winner_count = 0
    
    

    for row in readcsv:
        vote_count +=1
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
            
for key, value in candidates.items():
    percentage_votes[key] = round((value/vote_count) * 100, 2)
    
for key in candidates.keys():
    if candidates[key] > winner_count:
        winner = key
        winner_count = candidates[key]
    
print(vote_count)
print(candidates)
print(percentage_votes)
print(winner)


