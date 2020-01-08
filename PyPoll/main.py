import pandas as pd

df = pd.read_csv (r'election_data.csv') #Read CSV file

AllCnt = len(df) #Total vote count

Names = df.Candidate.nunique() #Total number of candidayes

VoterCnt = df.Candidate.value_counts() #Vote count by candidate

VotePercent = df.Candidate.value_counts()/AllCnt #Calculate percent of votes per candidate

#Create dataframe with candidate/percent/count of votes
VoteSummary = pd.DataFrame({ "Percent": VotePercent.apply('{:.3%}'.format), "Vote Count": VoterCnt}).reset_index()

#Print Output
print('Election Results')
print("--------------------------")

print("Total Votes: ", AllCnt) #Print the Total Election count

print("--------------------------")
for i in range(Names): #Print a loop through the name/Percent/Count of election results
    print(VoteSummary.iat[i,0], ":", VoteSummary.iat[i,1], " (",VoteSummary.iat[i,2],")" )

print("--------------------------")
print("Winner: ", VoteSummary.iat[0,0])  #Declare the Winnrer
