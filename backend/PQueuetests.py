#PQueue trials

from PQueue import PQueue
'''
immediate = 
not serious = '''
names = ['n1','n2','n3','n4','n5']
obj = PQueue()
for i in names:
    nature = str(input('Is the patient in immediate need of a doctor? (Yes/No) '))
    if nature.lower() == 'yes':
        obj.enqueue(0, i)
    elif nature.lower() == 'no':
        obj.enqueue(1, i)
    else:
        print('Invalid input.')

print("Len of High Priority Queue:", obj.__len__(0))
print("Len of Low Priority Queue:", obj.__len__(1))

print(obj.__str__(0))
print(obj.__str__(1))
print("Patient sent for consultation:", obj.dequeue())
print("Patient sent for consultation:", obj.dequeue())
print("Patient sent for consultation:", obj.dequeue())

print("Patient sent for consultation:", obj.dequeue())
print("After dequeue")
print(obj.__str__(0))
print(obj.__str__(1))