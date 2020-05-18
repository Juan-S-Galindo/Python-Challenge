import os
import csv

totalMonths = 0 #Declare  the globals to keep track of sums, min and max
maxIncrease = 0 
maxDecrease = 0 
indexMonthMax = 0
indexMonthMin = 0
totalIncome = 0
netIncomeTotal = 0
priorMonthProfitLoss = 0

def PyBank(row): #Function 

    global totalMonths #call global functions into the function.
    global maxIncrease
    global maxDecrease 
    global indexMonthMax
    global indexMonthMin
    global totalIncome
    global netIncomeTotal
    global priorMonthProfitLoss

    dateIndex = row[0] #declare the date index
    profitLossValue = int(row[1]) #declare the value of the groscolumn as integer for every row.

    
    totalMonths += 1 #Adds 1 for every iteration.
    totalIncome += profitLossValue #adds the total income

    def avgNetIncome(): #nested function to calculate average
            avgPL = netIncomeTotal / (totalMonths - 1)
            return avgPL

    if totalMonths > 1 : #start calculations after the first month.

        netIncome = profitLossValue - priorMonthProfitLoss #net income from the  current row P/L minus the prior month P/L
        netIncomeTotal += netIncome #Keep tally of the net income

        if netIncome > maxIncrease : #conditional test to add max/min and month index.
            maxIncrease = netIncome
            indexMonthMax = dateIndex
        elif netIncome < maxDecrease :
            maxDecrease = netIncome
            indexMonthMin = dateIndex
        
        priorMonthProfitLoss = profitLossValue #assigns the current P/L value to the prior month at the end of the iteration.
    
        s='-'*50
        return (f"{s}\n Financial Analysis \n \n Total Months: {totalMonths} \n Net Income: ${totalIncome} \n Average Change: ${round(avgNetIncome(),2)} \n Greatest Increase in Profits: {indexMonthMax} ({maxIncrease}) \n Greatest Decrease in Profits: {indexMonthMin} ({maxDecrease}) \n {s}")
        #returns the result.
    else:
        priorMonthProfitLoss += profitLossValue #assigns the first profit or loss value to the first month.

fileName = os.path.join('Resources','budget_data.csv') #path to file

with open(fileName, 'r') as csvfile: #Opens the file with reader settings as 'csvfile.

    csvreader = csv.reader(csvfile, delimiter=',') #csv reader  is assigned the csv file with delimiter: ,
    csvheader = next(csvreader,None) #to skip the header in the calculations. we would get error when adding the netIncome if we do not add this part.

    for row in csvreader: #for every row in the csvreader
        results = PyBank(row) #we assign the value returned at the end of the iteration to the variable RESULTs.

print(results) #print results.

textCopy = open('textCopy.txt','w') #creates copy as TXT
print(results, file=textCopy)
textCopy.close()