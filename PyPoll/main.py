import os
import csv

candidatesDict = {} #defines a global empty dictionary
totalVotes = 0 #Global vote tally.
candidateList = []

def PyPoll(row):
    global totalVotes
    global candidatesDict
    global candidateList
  
    candidateIndex = row[2]
    totalVotes += 1 #adds 1 vote to the total tally every time we do a row iteration.

    if candidateIndex in candidatesDict:
        candidatesDict[candidateIndex] += 1 
    else:
        candidatesDict.update({candidateIndex:1})

    keyMax = max(candidatesDict, key=candidatesDict.get)

    if (totalVotes+1 == csvTotalLines):
        s='-'*20
        textCopy = open('textCopy.txt','w') #creates copy as TXT
        print(s, file=textCopy)
        print("ELECTION RESULTS", file=textCopy)
        print(s, file=textCopy)
        print(f"Total Votes: {totalVotes}", file=textCopy)
        print(s, file=textCopy)

        def votes():
            for i in candidatesDict:
               print (f"{i}: {(round(candidatesDict[i]/totalVotes)*100,2)}% ({candidatesDict[i]})", file=textCopy)
        votes()

        print(s, file=textCopy)
        print(f"Winner: {keyMax}", file=textCopy)
        print(s, file=textCopy)
        textCopy.close()

        print(s)
        print("ELECTION RESULTS")
        print(s)
        print(f"Total Votes: {totalVotes}")
        print(s)

        def votesT():
            for i in candidatesDict:
               print (f"{i}: {round((candidatesDict[i]/totalVotes)*100,2)}% ({candidatesDict[i]})")
        
        votesT()
        
        print(s)
        print(f"Winner: {keyMax}")
        print(s)

fileName = os.path.join('Resources','election_data.csv')

with open(fileName, 'r') as csvfile: #Opens the file with reader settings as 'csvfile.

    csvreader = csv.reader(csvfile, delimiter=',') #csv reader  is assigned the csv file with delimiter: .
    csvTotalLines = len(list(open(fileName)))
    csvheader = next(csvreader,None) #to skip the header in the calculations. 

    for row in csvreader: #for every row in the csvreader
        PyPoll(row)


       



    
        



