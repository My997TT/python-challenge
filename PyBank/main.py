import pandas as pd
import sys

df = pd.read_csv (r'budget_data.csv') #Load CSV file to read

#Create dataframe RChange to hold Date/Profit/Losses/Monthly Change in profits
RChange = pd.DataFrame({"Date":df['Date'], "Profit/Losses":df['Profit/Losses'],"MonthlyChange":df['Profit/Losses'].shift(-1)-df['Profit/Losses']})

MyMax = RChange['MonthlyChange'].max() #Find Max value of Changes between months in dataframe
iMax = RChange.MonthlyChange.idxmax()  #Find index in dataframe RChange of Max change between months

MyMin = RChange['MonthlyChange'].min() #Find Min value of Changes between months in dataframe
iMin = RChange.MonthlyChange.idxmin()  #Find index in dataframe RChange of Min change between months

MyAvg = round(RChange['MonthlyChange'].mean(),2) #Find Avg value of Changes between months in dataframe


#Print Results to Screen
print('Financial Analysis')
print('---------------------------')
print ('Total Month :  ' + str(len(df))) #Find total number of records in CSV file
print('Total: $' +str(df['Profit/Losses'].sum())) #Sum the Profit/Losses for the CSV file
print('Average  Change: $' +str(MyAvg))
print('Greatest Increase in Profits: ',RChange.iat[iMax+1,0], '($', MyMax,')') #Print month change using iMax index 
print('Greatest Increase in Profits: ',RChange.iat[iMin+1,0], '($', MyMin,')') #Print month change using iMin index

#Print Results to Text File PyBank.txt
stdoutOrigin=sys.stdout
sys.stdout=open("PyBank.txt","w")

#Print Results
print('Financial Analysis')
print('---------------------------')
print ('Total Month :  ' + str(len(df))) #Find total number of records in CSV file
print('Total: $' +str(df['Profit/Losses'].sum())) #Sum the Profit/Losses for the CSV file
print('Average  Change: $' +str(MyAvg))
print('Greatest Increase in Profits: ',RChange.iat[iMax+1,0], '($', MyMax,')') #Print month change using iMax index 
print('Greatest Increase in Profits: ',RChange.iat[iMin+1,0], '($', MyMin,')') #Print month change using iMin index

sys.stdout.close()
 