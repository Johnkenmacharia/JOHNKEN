# import functions

# x=functions.add(12,43)

# print   (x)


# y=functions.subtract(43,23)
# print(y)/

import operators
import others
import trig
#build a better calculator
x=others.cube(9)
y =operators.add(23,55)
print (x)
print (y)


#get numbers
operator =input("enter operator:")
if operator=="cube":
    num =eval(input("enter a number:"))
    x=others.cube(num)
    print(x)

elif operator == "sin":
    angle=eval(input("enter angle in degrees:"))
    sin_of_angle =trig.get_sine(angle)
    print(sin_of_angle)

elif operator =="tan":
    angle=eval(input("enter angle in degrees:"))
    print(trig.get_tan(angle))

elif operator =="cos":
    angle = eval(input("enter angle in degrees"))
    print(trig.get_cos(angle))


else:

     num1=eval(input("enter a number 1:"))
     num2=eval(input("enter number 2:"))


     if operator =="+":
        x=operators.add(num1,num2)
        print(x)

     elif operator =="-":
        X=operators.subtract(num1,num2)
        print(X)

     elif operator =="/":
        x=operators.divide(num1,num2)
        print(x)

     elif operator =="*" or "x" or "X":
        x=operators.multiply(num1,num2)
        print(x)



