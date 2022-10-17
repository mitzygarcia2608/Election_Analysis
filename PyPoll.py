#The data we need to retreive
#The Total number of votes cast
# A complete list of candidates who recieved votes
#The percentage of votes each candidate won
# THe total number of votes each candidate won
#The Winner of the election based on popular vote

import csv
import os
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save= os.path.join("analysis","election_analysis.txt")
#1. get total votes and create accumulator
total_votes=0
candidate_options=[]
candidate_votes={}
vote_percentage=(candidate_votes/total_votes)*100
winning_candidate=""
winning_count=0
winning_percentage=0


with open(file_to_load) as election_data:
 

    file_reader=csv.reader(election_data)
    
    #print header row
    headers = next(file_reader)
    print(headers)


    #print each row in the csv file
    for row in file_reader:
       #add the total vote count
         total_votes+= 1
         #print candidate name in each row
         candidate_name =row[2]

         if candidate_name not in candidate_options:
          #add the candidates name to the candidate options list
             candidate_options.append(candidate_name)

             # begin to track the candidate votes
             candidate_votes[candidate_name]=0
         candidate_votes[candidate_name]+=1


    for cadidate_name in candidate_votes:
        #change candiate votes into just votes
        votes=candidate_votes[candidate_name]
        #calculate the percentage of votes
        vote_percentage = float(votes) /float(total_votes)*100
        if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

         # To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.
print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
print(winning_candidate_summary)