# FizzBuzz Basic VERSION 2
#Raphael Capon
#2017-05-28

# prints integers from 1 to specified value, replacing the following:
#     -multiples of 3 with the string "fizz"
#     -multiples of 5 with the string "buzz"
#     -multiples of both with "fizzbuzz"

import sys

user_n = ""
target = 0


if len(sys.argv) > 1:
    
    user_n = sys.argv[1]
    
else:
    
    user_n = input("enter the target value")


while True:
    
    try:
        
        target = int(user_n)
        
        break
        
    except ValueError:
        
        user_n = input("enter the target value")
    
    
for n in range(1,target+1):
    
    if n % 15 == 0:
        
        print("fizzbuzz")
        
    elif n % 5 == 0:
        
        print ("buzz")
    
    elif n % 3 == 0:
        
        print("fizz")
        
    else:
    
        print(n)
    

    


