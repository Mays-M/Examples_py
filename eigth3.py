t=True
n=True
f=True
import math

print("Calculator")
while t:
        num1=input("Give the first number:")
        try:
            num1=int(num1)
            t=False
            
        except(TypeError,ValueError):
            print("This input is invalid.")
            t=True
while f:
        num2=input("Give the second number:")
        try:
            num2=int(num2)
            f=False
        except(TypeError,ValueError):
            print("This input is invalid.")
            f=True
   
       
      
while n :
        print("(1) +")
        print("(2) -")
        print("(3) *")
        print("(4) /")
        print("(5)sin(number1/number2)")
        print("(6)cos(number1/number2)")
        print("(7)Change numbers")
        print("(8)Quit")
        print("Current numbers:",+num1,+num2)
        select=input("Please Select something (1-6):")
        if(select=='1'):
            print("The result is:",+(num1+num2))
            n=True
        elif(select=='2'):
            print("The result is:",+(num1-num2))
            n=True
        elif(select=='3'):
            print("The result is:",+(num1*num2))
            n=True
        elif(select=='4'):
            print("The result is:",+(num1/num2))
            n=True
        elif(select=='5'):
            print("The result is:",+ (math.sin(num1/num2)))
            n=True
        elif(select=='6'):
            print("The result is:",+ (math.cos(num1/num2)))
            n=True
        elif(select=='7'):
            t=False
        elif(select=='8'):
            print("Thank you!")
            t=False
            f=False
            n=False
        else:
            n=True
    
