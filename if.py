#ask for input 
#check if input is negative
#if negative,tell user wrong input
#if positive,check greater than 50 
#if greater than 50 divide by 2
#if less than 50,tell user number is less than 50
num =eval(input("enter a number"))
if num <0:
    print("wrong input")
else:
    if num > 50:
        x = num/2
        print(x) 
    else:
        print("number is less than 50")       