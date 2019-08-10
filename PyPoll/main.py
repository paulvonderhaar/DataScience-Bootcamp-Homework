#Import libraries
import csv
#Define variables
count=0
candidates={}
percentages={}
max=-1
winner=''

#Open data, and split the resulting string up into a list
with open("Poll.csv") as csvfile:
    next(csvfile)
    for line in csvfile:
        count=count+1
        info=line.split(",")
        #Find the candiadte name inside the resulting list
        candidate=info[1]+" "+info[2]
        #If the candiate already has a key value pair in the dictionary, add one to the value
        if candidate in candidates:
            candidates[candidate]+=1
        #If the candiate doesn't have a key value pair, create a new key value pair with the candiate as the key and a value of one
        else:
            candidates[candidate]=1
#For each candiate, create a new dictionary with the key of the candiate name, and the value of hte percent of votes won
for i in candidates:
    percentages[i]=round(candidates[i]/count,2)*100
    if(percentages[i]>max):
        max=percentages[i]
        winner=i

f= open("reults.txt","w+")
for i in (candidates):
    print(str(i)+" recieved "+str(percentages[i])+" of the vote, with "+str(candidates[i])+"% total votes")
    f.write(str(i)+" recieved "+str(percentages[i])+" of the vote, with "+str(candidates[i])+"% total votes\n")
    
    
print(winner+" is the winner")
f.write(winner+" is the winner")
f.close()
    