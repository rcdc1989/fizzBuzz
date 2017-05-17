# FizzBuzz Basic
#Raphael Capon
#2017-05-28

# prints integers from 1 to specified value, replacing the following:
#     -multiples of 3 with the string "fizz"
#     -multiples of 5 with the string "buzz"
#     -multiples of both with "fizzbuzz"


target = 100 # value we are counting to
answer = "" # string to store our answer

print "FizzBuzz counting up to {}".format(target)

for i in range(1,target):   # loop using variable i, from 1 to 100
    
    if i%3 == 0: #use modulo operator find remainder of i/3,  0 for multiples of 3
    
        answer = "fizz"
    
    if i%5 == 0: # do the same for five
    
        answer = answer + "buzz"
        
    if answer =="": # if neither fizz nor buzz, set answer to counter, i
        
        answer = str(i)
    
    print answer + "\n"
    answer = ""
