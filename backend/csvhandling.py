import csv

class SearchandDisplay():
    with open("patientrecord.csv", 'r') as csvfile:
        rows = csv.reader(csvfile)
        k =0

        while k==0:
        
            try:
                option = int(input("1 for searching with Name\n2 for searching with Phone NO\nEnter option: "))
            
                i = 0
                while i == 0:
                    if option==1:
                        def searchName():
                            j =0
                    
                            while j==0:
                        
                                global userinput
                                userinput = input("Enter Name of the patient with first letter caps: ")
                            
                                if userinput.isalpha():
                                    if userinput[0].isupper():
                                        break
                            
                                    elif userinput[0].isupper()==False:
                                        print("Invalid input. Enter name with first letter caps")
                                        print("Try again")
                                        j =0
 
                                else:
                                    print("Invalid input. Enter name with alphabets only.(First letter in caps) ")
                                    print("Try again")
                                    j =0

                        searchName()
                        k=1
                        break
                        

                    elif option==2:
                        def searchPhone():
                            j = 0
                    
                            while j==0:
                                try:
                                    userinput1 = int(input("Enter Phone No of the patient: "))
                                    global userinput
                                    userinput = str(userinput1)
                                    if len(userinput) ==10 :
                                        
                                        break
                            
                                    elif len(userinput) !=10 :
                                        print( "Invalid input. Enter phone number with 10 numbers")
                                        print("Try again")
                                        pass 

                                except ValueError:
                                    print( "Invalid input. Enter phone number with 10 numbers(no letters)")
                                    print("Try again")
                                    pass
                
                        searchPhone()
                        k=1
                        break
                        

                    else:
                        print("Enter 1 or 2 only")
                        print("Try again")
                        k=0
                        break
            
            except ValueError:
                print("Enter 1 or 2 only")
                print("Try again")
                k=0

        
        _verifylist = []
        z =0
        for row in rows:
            if userinput in row:
                print("Patient found")
                _verifylist.append(z)
                print(row)

        if len(_verifylist)==0:
            print("Patient not found")
            

SearchandDisplay()
