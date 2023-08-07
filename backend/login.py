import csv

def signin():
    flag=0
    print ("""
  ____ ___ ____ _   _     ___ _   _ 
 / ___|_ _/ ___| \ | |   |_ _| \ | |
 \___ \| | |  _|  \| |    | ||  \| |
  ___) | | |_| | |\  |    | || |\  |
 |____/___\____|_| \_|   |___|_| \_|""")
    print()
    uncheck=input("Enter your username : ")
    pwdcheck=input('Enter Your Password : ')
    print()
    with open("USER DATA FA.csv",'r') as f :
        data=list(csv.reader(f))
        for i in range(len(data)):
            if data[i][2]==uncheck and data[i][3]==pwdcheck:
                flag=1
                print("****** LOGIN SUCCESFUL !! ******")
                print("Welcome",data[i][1],data[i][0].title())
                print()
            
        if flag==0:
            print("****** LOGIN FAILED !! CHECK YOUR USERNAME OR PASSWORD... ******")
            print()
            signin()
            
def signup():    
    print("""
 ____ ___ ____ _   _    _   _ ____  
/ ___|_ _/ ___| \ | |  | | | |  _ \ 
\___ \| | |  _|  \| |  | | | | |_) |
 ___) | | |_| | |\  |  | |_| |  __/ 
|____/___\____|_| \_|   \___/|_|

 FOR DOCTORS AND RECEIPTIONISTS""")

    print()
    fname=input("Enter Your Name : ")
    prof=input("Doctor/Recieptionist (D/R): ").upper()
    if prpwdof=="D":
        prof="Doctor"
    elif prof=="R":
        prof="Recieptionist"
    un=input("Enter Your Username : ")
    if un=="":
        print("**** Sorry, Username Can't Be Empty !! ****")
        signup()
    f=open("USER DATA FA.csv","a+")
    data=list(csv.reader(f))
    for i in range(len(data)):
        if un==data[i][1]:
            print()
            print("**** Username Taken. Please Try A Different One !! ****")
            signup()
    pwd=input('Enter Your Password : ')
    if len(pwd)<8:
        print()
        print("**** Sorry, Length Of Password Should Be 8 or More Characters ****")
        signup()
    if un==pwd:
        print()
        print("**** Sorry, Username and Password Should Not Be The Same ****")
        signup()
    else:
        repwd=input('Re-Enter your Password : ')
        if pwd==repwd:
            try:
                num=input("Enter Your Phone Number : ")
                if len(num)<10 and len(num)>10:
                    print()
                    print("**** Sorry, Length Of Password Should Be 8 or More Characters ****")
                    signup()
                gender=input("Enter Your Gender ( M/F/T ): ")
                email=input ("Enter Your E-Mail Id : ")
                data=[fname,prof,un,pwd,num,gender,email]
                print()
                f=open("USER DATA FA.csv",'a',newline='')
                cw=csv.writer(f)
                cw.writerow(data)
                f.close()
                print("""
88888888888 888    888        d8888 888b    888 888    d8P      Y88b   d88P  .d88888b.   888     888 
    888     888    888       d88888 8888b   888 888   d8P        Y88b d88P  d88P" "Y88b  888     888 
    888     888    888      d88P888 88888b  888 888  d8P          Y88o88P   888     888  888     888 
    888     8888888888     d88P 888 888Y88b 888 888d88K            Y888P    888     888  888     888 
    888     888    888    d88P  888 888 Y88b888 8888888b            888     888     888  888     888 
    888     888    888   d88P   888 888  Y88888 888  Y88b           888     888     888  888     888 
    888     888    888  d8888888888 888   Y8888 888   Y88b          888     Y88b. .d88P  Y88b. .d88P 
    888     888    888 d88P     888 888    Y888 888    Y88b         888      "Y88888P"    "Y88888P"  
                                                                                                   
                          <<<<<<< For Registering To FAST AID >>>>>>> """)
                print()
            except ValueError:
                print()
                print("**** Phone Number Should Only Be In Numbers !!! ****")
                signup()
        else:
            print()
            print("**** Sorry Re-entered Password Incorrect !!! ****")
            signup()

signup()
signin()
