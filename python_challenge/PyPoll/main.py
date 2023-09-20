#python program to analyze the election voting data
import csv

ballot_id = []
#dictionary to store participated candidates and total votes each candidate received
candidateVote_dict = {} 
output = [] #list to store output data

#define a function to copy analysis data to a text file
def copy_results_tofile(file_path,values):
    with open(file_path, 'w') as file:
        file.write(f"Election Results\n\n")
        file.write("-----------------------------\n\n")  
        file.write(f"Total Votes: {values[0]}\n")
        file.write(f"-----------------------------\n\n")  
        file.write(f"{values[1]}: {values[2]}% ({values[3]})\n\n")
        file.write(f"{values[4]}: {values[5]}% ({values[6]})\n\n")
        file.write(f"{values[7]}: {values[8]}% ({values[9]})\n\n")
        file.write("-----------------------------\n\n") 
        file.write(f"Winner: {values[10]}\n\n")
        file.write("-----------------------------\n") 

 
#opening csv file to read and analyze voting data
with open("Resources/election_data.csv", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader, None) #skip header row

#Loop through each row in the CSV and 
#create a list of participated candidates 
    for voting_data in csvreader:
        ballot_id.append(voting_data[0])
        candidate = voting_data[2]
        if candidate in candidateVote_dict:
            candidateVote_dict[candidate] += 1
        else:
            candidateVote_dict[candidate] = 1
    

#calculate total cast vote
total_votes = len(ballot_id)
output.append(total_votes) #adding output value to output[]

print("Election Results\n")
print("-----------------------------\n")   
print(f"Total Votes: {total_votes}\n")
print("-----------------------------\n")  

candidates = list(candidateVote_dict.keys())
VotePerCandidate = list(candidateVote_dict.values())

#calculate total votes and percentage of votes each candidate received
i = 0
for votes in VotePerCandidate:
    vote_percentage = round((votes/total_votes)*100 ,3)
    print(f'{candidates[i]}: {vote_percentage}% ({votes})\n')
    output.append(candidates[i])
    output.append(vote_percentage)
    output.append(votes)
    i +=1 

#find winner based on max vote
winner = " "
winning_vote = 0
winning_vote = max(VotePerCandidate)
index = VotePerCandidate.index(winning_vote)
winner = candidates[index]
output.append(winner) 

output.append(winner)   
print("-----------------------------\n") 
print(f"Winner: {winner}")
print("-----------------------------\n") 

#call function to copy output data to a text file
path_toFile = "analysis/result.txt"
copy_results_tofile(path_toFile,output)

