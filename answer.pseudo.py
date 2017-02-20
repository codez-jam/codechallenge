# Program 

# import the random module
import random

def wingify():
    n='y';
    while(n!='n'):
     a=(random.randint(6,15))     #to generate a random number between 6 and 15.
     s=input("Enter a name:")     # Input Name.
     print("Name GeneratedNumber",s,a)  #Display the Required Output(along with random number).
     n=input("Do you want to continue(y/n):") # Again (y/n) ?
print("Program Started ")       #Just a Pointer Program Start.
wingify()
print("Program Ends")            # Another Pointer Program Ends.
     

