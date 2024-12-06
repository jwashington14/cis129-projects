#Jessica Washington 
CIS-129 Prog & Problem Solve 
#Program: Lab 5: The Bottle Return Program that keeps track of total number of returned bottles 
#Date: 12/4/2024



def getBottles():
    #return the total number of bottles for the week
    no_of_days=7
    totalBottles=0
    todayBottles=0
    counter=0
    while counter<7:
        print("Enter number of bottles returned for day #"+str((counter+1))+":")
        todayBottles=int(input())
        counter+=1
        totalBottles+=todayBottles
    print(totalBottles)  
    return totalBottles

def calcPayout(totalBottles):
    #return total payment for the week
    payout_per_bottle=0.10
    totalPayout=0 
    totalPayout=totalBottles*payout_per_bottle
    return totalPayout

totalBottles=0
counter=1 
