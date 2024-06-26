import sys

userinput=input("Give a number:")
while True:
    try:
        userinput=int(userinput)
        print("The input was suitable!")
        break
    except :
        print("The input was malformed.")
        break
     
    
