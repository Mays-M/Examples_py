import os

def tester(givenstring="too short"):
        result=len(givenstring)
        if result <10  :
            return 0
            
        
        if(len(givenstring) >=10 ):
            return 1
def main():
        while True:
            userinput=input("Write something: ")
            if(userinput=='quit'):
                break
            else:
                tester(userinput)
                if tester(userinput)==True :
                    print(userinput)
                    if 'x' in userinput:
                        print("X spotted!")
                    if 'X' in userinput:
                        print("X spotted!")

                else:
                    print("Too short")
                
    
    
    
if __name__=="__main__":
    main()
