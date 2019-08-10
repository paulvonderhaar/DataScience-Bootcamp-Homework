import csv


# In[16]:


total=0
min=999999999
minMonth=''
maxMonth=''
max=-999999999
count=0

with open("bank.csv") as csvfile:
    myreader=csv.reader(csvfile)
    a=next(myreader)
    for line in myreader:
        count+=1
        total=total+float(line[1])
        if(float(line[1])>=max):
            max=float(line[1])
            maxMonth=line[0]
        if(float(line[1])<=min):
            min=float(line[1])
            minMonth=line[0]
    count=round(count)
    total=round(total)
    
    min=round(min)
    max=round(max)
    
    print("The number of months is : $"+str(count))
    average=round(total/count,2)
    print("The total amount of money is $: "+str(total))
    print("The average monthly change is $: "+str(average))
    print("The lowest monthly change was the month "+minMonth+" with a value of : $"+str(min))
    print("The highest monthly change was the month "+maxMonth+" with a value of : $"+str(max))

f= open("results.txt","w+")
f.write("The number of months is : $"+str(count)+"\n"+
       "The total amount of money is $: "+str(total)+"\n"+
       "The average monthly change is $: "+str(average)+"\n"+
       "The lowest monthly change was the month "+minMonth+" with a value of : $"+str(min)+"\n"+
       "The highest monthly change was the month "+maxMonth+" with a value of : $"+str(max))
f.close()






