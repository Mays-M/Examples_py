
def check(numb1,numb2):
 t=True
 while t:
        try:
            numb1=int(numb1)
            return numb1
        except :
            print("This input is invalid.")
            
        try:
            num2=int(num2)
            return num2
        except:
            print("This input is invalid.")

def main():
    while True:
        num1=input("num1")
        num2=input("num2")
        check(num1,num2)
if __name__=="__main__":
    main()
