Jessica Washington
CIS129 Prog & Problem Solv I
Module 11: Lab 
11/27/2024




1.

with open('grades.txt', 'w') as file: 
    
    while True: 
        grade =input("Enter a grade (or '-1' to quit): ") 
        if grade.lower() =='-1': 
            break 
        file.write(grade +'\n') 


2.

with open('grades.txt', 'r') as file: 
    grades = file.read().splitlines()
    grades = [float(grade) for grade in grades] 
    
    print("Individual grades: ", grades) 
    
    total = sum(grades) 
    count = len(grades) 
    
    average = total / count
    
    print("Total: ", total) 
    print("Count: ", count) 
    print("Average: ", average)

3.

import csv

with open('grades.csv', 'w', newline='') as file: 
    
    writer = csv.writer(file) 
    
    writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3']) 
    
    while True: 
        first_name =input("Enter the student's first name (or 'q' to quit): ") 
        
        if first_name.lower() =='q': 
            break 
        last_name =input("Enter the student's last name: ") 
        exam1 =int(input("Enter the student's exam 1 grade: ")) 
        exam2 =int(input("Enter the student's exam 2 grade: ")) 
        exam3 =int(input("Enter the student's exam 3 grade: ")) 
        
        print([first_name, last_name, exam1, exam2, exam3])
