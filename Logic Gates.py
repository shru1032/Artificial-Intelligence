#Implementation of AND, OR and XOR logic gates in Python
def AND(a,b):
 if (a==1 and b==1):
 return 1
 else:
 return 0

def OR(a,b):
 if (a==1 or b==1):
 return 1
 else:
 return 0
5
def XOR(a,b):
 if (a!=b):
 return 1
 else:
 return 0
a = int(input("Enter A(0/1): "))
b = int(input("Enter B(0/1): "))
if ((a==0 or a==1) and (b==0 or b==1)):
 print("****Main Menu****")
 print("1. AND")
 print("2. OR")
 print("3. XOR")
 print("4. Exit")
 choice = int(input("Enter your choice here: "))
 if (choice==1):
 print("A and B: ", AND(a,b))
 elif (choice==2):
 print("A or B:", OR(a,b))
 elif (choice==3):
 print("A xor B: ", XOR(a,b))
 else:
 pass
else:
 print("Invalid Input!")
