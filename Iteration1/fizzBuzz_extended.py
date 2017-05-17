# FizzBuzz extended (AKA: fizzbuzzfloozeshoes)
#Raphael Capon
#2017-05-28

#BASIC:
# prints integers from 1 to specified value, replacing the following:
#     -multiples of 3 with the string "fizz"
#     -multiples of 5 with the string "buzz"
#     -multiples of both with "fizzbuzz"

#EXTRA CHALLENGE:
# If the user supplies a value at the command line when script runs, we'll use that value.
# Otherwise, we'll use the input() function to get a value from the user

#EXTENDED:
#Extend fizzbuzz concept: a more general case which uses a dictionary to add expressions other than fizz or buzz
#eg: 6 --> flooze, 8 --> shoes


import sys


data = {"3":"fizz", "5":"buzz", "6":"flooze", "8":"shoes"}# enter "fizzbuzz" data as a dictionary 


try: #attempt to get target value from argv list
    
    target = int(sys.argv[1])
    print(sys.argv[1])
    
except(IndexError,TypeError): #if no argument is present or argument is not valid, get target value from user
    
    try:
        
        target = input("To what number will you fizzbuzz?")
        
        if target == 0 or not target is int: #check if input is valid
            
            raise TypeError
        
    except(TypeError, NameError): #handle case where input is not valid
        
        print("you must supply an integer. quitting...")
        quit()
        

    
answer = "" # string to store our answer

print("FizzBuzz counting up to {}".format(target))

for i in range(1,target+1):  # loop using variable i, from 1 to 100
    
    
    for j in sorted(data.keys()): #cycle through dictionary keys, checking if i is a factor, if so, we add appropriate "word" to answer string
     
        if i % int(j) == 0:
            
            answer = answer + data.get(j)
        
    if answer =="": # if no "words" apply, set answer to counter, i
        
        answer = str(i)
    
    print(answer + "\n")
    answer = "" # Reset answer variable