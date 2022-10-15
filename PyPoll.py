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

with open(file_to_load) as election_data:
 

    file_reader=csv.reader(election_data)
    
    #print header row
    headers = next(file_reader)
    print(headers)
#using the open function with the"w" mode we will write data to the text file



