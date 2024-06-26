import os
t=True
while t:
    with open("notebook.txt","a") as content:
        print("(1)Read the notebook")
        print("(2)Add note")
        print("(3)Empty the notebook")
        print("(4)Quit")
        select=input("Please select one:")
        if(select=='1'):
         with open("notebook.txt","r") as f:
          s=f.readlines()
          print(s)
        elif(select=='2'):
         note=input("Add note:\n")
                    
         f2=content.write(note)
         f3=content.write('\n')
         print (note + '\n')
        
        elif(select=='3'):
          content.truncate(0)
          print("Note deleted")
      
        elif(select=='4'):
         print("Notebook shutting down, thank you.")
         t=False
        else:
         j=0
