print("Calculator")
num1=int(0)
num2=int(0)
t=True
while t:
 num1=int(input("Give the first number:"))
 num2=int(input("Give the second number:"))
 while t :
   print("(1)+")
   print("(2)-")
   print("(3)*")
   print("(4)/")
   print("(5)Change numbers")
   print("(6)Quit")
   print("Current numbers",+num1,+num2)
   select=input("Please select something (1-6):")
   if(select=='1'):
    print("The result is:",+(num1+num2))
    t=True
   elif(select=='2'):
    print("The result is:",+(num1-num2))
    t=True
   elif(select=='3'):
    print("The result is:",+(num1*num2))
    t=True
   elif(select=='4'):
    print("The result is:",+(num1/num2))
    t=True
   elif(select=='5'):
     break
   elif(select=='6'):
    print("Thank you!")
    t=False
    
   else:
     t=True
