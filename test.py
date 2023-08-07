import csv
f=open("USER DATA FA.csv","r")
a=csv.reader(f)
acc=[]    
        
for row in a:
    acc.append(row)

print(acc)
