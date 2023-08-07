import csvhandling
import csv
from PQueue import PQueue

obj = csvhandling.SearchandDisplay()
_lst =[]
if len(obj._verifylist) == 0:
    j =0
                    
    while j==0:
                        
                        try:
                            global userinput
                            name = input("Enter Name of the patient with first letter caps: ")
                            
                            if name[0].isupper():
                                break
                            
                            elif name[0].isupper()==False:
                                print("Invalid input. Enter name with first letter caps")
                                print("Try again")
                                j =0

                        except KeyError():
                            raise "Invalid input. Enter name to search patient."


    l = 0
                    
    while l==0:
                        try:
                            age = int(input("Enter age of the patient: "))
                            if age <=125:
                                break
                            elif age >125 :
                                print( "Invalid input. Enter the correct age")
                                print("Try again")
                                pass

                        except KeyError():
                            raise "Invalid input. Enter the age"
                            raise "Try again" 
    gender = input("Enter the Patient's gender :")
    i = 0
                    
    while i==0:
                        try:
                            phone1 = int(input("Enter Phone No of the patient: "))
                            global phone
                            phone = str(phone1)
                            if len(phone) ==10:
                                break
                            elif len(phone) !=10 :
                                print( "Invalid input. Enter phone number with 10 numbers")
                                print("Try again")
                                pass

                        except KeyError():
                            raise "Invalid input. Enter Phone no to search patient"
                            raise "Try again"   
    
    k = 0
                    
    while k==0:
                        try:
                            email1 = input("Enter email id of the patient: ")
                            global email
                            email = str(email1)
                            if "@" in email:
                                break
                            elif "@"  not in email :
                                print( "Invalid input. Missing character @")
                                print("Try again")
                                pass

                        except KeyError():
                            raise "Invalid input. Enter email id"
                            raise "Try again" 
    
    issue = input("Enter the Patient's issue:")
    prescription = input("Enter the Prescription suggested:")
    
    _lst.append(name)  
    _lst.append(age)
    _lst.append(gender)
    _lst.append(phone)
    _lst.append(email)
    _lst.append(issue)
    _lst.append(prescription)
    
    header = ['Name','Age','Gender','Mobile no','email','Issue','Prescription']
    file1 = open ('patientrecord.csv','r')
    reader = csv.reader(file1)
    
    new = []
    for row in reader:
       new. append (row)
    file1.close()
    with open('patientrecord.csv', mode='w') as patientrecord:
        patient = csv.writer(patientrecord, delimiter=',')
        for i in range (len(new)):
                patient.writerow(new[i])
        patient.writerow([name,age,gender,phone,email,issue,prescription])

    cal = PQueue()
    p = int(input ("Enter your priority:"))
    cal.enqueue(p,_lst)
    cal.__str__(p)    
    
else:
    cal = PQueue()
    p = int(input ("Enter your priority:"))
    cal.enqueue(p,_lst)
    cal.__str__(p)    
    