import time
import sys
print("No default notebook was found, created one.")

def files():
    filename=input("Give the name of the new file:")
    return filename
    

def main(filename='notebook.txt'):
    while True:
        print("Now using file",filename)
        with open(filename,"a") as content:
            print("(1) Read the notebook")
            print("(2) Add note")
            print("(3) Empty the notebook")
            print("(4) Change the notebook")
            print("(5) Quit")
            select=input("Please select one: ")
            if(select=='1'):
                with open(filename,"r") as f:
                    s=f.read()
                    print(s)
            elif(select=='2'):
                note=input("Write a new note: ")
                note =note +':::'
                note +=time.strftime('%x %x')
                f2=content.writelines(note +'\n')
            elif(select=='3'):
                content.truncate(0)
                print("Notes deleted.")
            elif(select=='4'):
                try:
                    f=files()
                finally:
                    if (f!='notebook.txt'):
                            print("No notebook with that name detected, created one.")
                main(f)
            else:
                print("Notebook shutting down, thank you.")
                sys.exit(0)
                break
                
            
               
if __name__=="__main__":
    main()
	  
