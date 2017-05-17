# FizzBuzz Extra Challenge
#Raphael Capon
#2017-05-28
#BASIC
# prints integers from 1 to specified value, replacing the following:
#     -multiples of 3 with the string "fizz"
#     -multiples of 5 with the string "buzz"
#     -multiples of both with "fizzbuzz"

#EXTRA CHALLENGE:
# If the user supplies a value at the command line when script runs, we'll use that value.
# Otherwise, we'll use the input() function to get a value from the user

import sys

try: #attempt to get target value from argv list
    
    target = int(sys.argv[1])
    print(sys.argv[1])
    
except(IndexError,TypeError): #if no argument is present or argument is not valid, get target value from user
    
    
    try:
        
        target = input("To what number will you fizzbuzz?")
        
            if target == 0 or not target is int: #check if input is valid
            
            raise TypeError
        
    except(TypeError, NameError): # handle case where input is invalid
        
        print("you must supply an integer. quitting...")
        quit()
        
answer = "" # string to store our answer

print("FizzBuzz counting up to {}".format(target))

for i in range(1,target+1):   # loop using variable i, from 1 to 100
    
    if i%3 == 0: #use modulo operator find remainder of i/3 (0 for multiples of 3)
    
        answer = "fizz"
    
    if i%5 == 0: # do the same for five
    
        answer = answer + "buzz"
        
    if answer =="": # if neither fizz nor buzz, set answer to counter, i
        
        answer = str(i)
    
    print(answer + "\n")
    answer = "" # Reset answer variable
