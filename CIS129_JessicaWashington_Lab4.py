#Module 4 Lab-4
#Jessica Washington 
#11/10/2024
#Program: Modifies bonus portion and eliminate the day off program 

#the main function
def main():
    monthlySales = getSales() #call to get sales 
    salesIncrease = getIncrease() # call to get sales increase

#This function gets the monthly sales
def getSales():
      monthlySales= getSales("Enter the monthly sales: ")
      monthlySales = float(input(prompt))
      return monthlySales

#This function gets the percent of increase in sales
def getIncrease():
       salesIncrease = input('Enter percent of sales increase.For example 4% should be entered as 4: ')          
       salesIncrease = float(salesIncrease)    
       salesIncrease = salesIncrease / 100      
       return salesIncrease

#call to get the store bonus
       storeAmount = 0
       return storeAmount

#This function determines the storeAmount bonus
def storeBonus(monthlySales):
    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >=100000:
        storeAmount = 5000
    elif monthlySales >=90000:
        storeAmount = 4000
    elif monthlySales >=80000:
        storeAmount = 3000
    else:
        storeAmount = 0
        return storeAmount

#This function determines the empAmount bonus 
def empBonus(salesIncrease):
    if salesIncrease >= .05:
        EmpAmount = 75
    elif salesIncrease >= 0.04:
        EmpAmount = 50
    elif salesIncrease >= .03:
        empAmount = 40
    else:
        empAmount = 0
    return empAmount

#call to get employee Amount
empAmount = salesIncrease()

#This function prints the bonus information 
def printBonus( storeAmount, empAmount):
    print("The store bonus amount is $", storeAmount)
    print("The employee bonus amount is $", empAmount)
    if (storeAmount == 6000 ) and (empAmount == 75):
        print('Congrats! You have reached the highest bonus amounts possible! ')

#calls main
main()


