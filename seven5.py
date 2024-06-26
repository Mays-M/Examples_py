t=True
import math

print("Calculator")

while t :
	num1=int(input("Give the first number:"))
	num2=int(input("Give the second number:"))
	while t :
		print("(1) +")
		print("(2) -")
		print("(3) *")
		print("(4) /")
		print("(5)sin(number1/number2")
		print("(6)cos(number1/number2")
		print("(7)Change numbers")
		print("(8)Quit")
		print("Current numbers:",+num1,+num2)
		select=input("Please Select something (1-8):")
		
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
					print("The result is:",+ (math.sin(num1/num2)))
					t=True

		elif(select=='6'):
					print("The result is:",+ (math.cos(num1/num2)))
					t=True
		
				
		elif(select=='7'):
					break
		elif(select=='8'):
			print("Thank you!")
			t=False
			t=False
		else:
					break
