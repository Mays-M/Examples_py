
mylist=[]
t=True

while t:
        print("Would you like to")
        print("(1)Add or")
        print("(2)Remove items or")
        choice=int(input("(3)Quit?: "))
        if (choice==1) :
            add=input("What will be added?: ")
            mylist.append(add)
        elif (choice==2):
            print("There are",len(mylist),"items in the list.")
            itemdeleted=int(input("Which item is deleted?: "))
            t=True
            try:
                mylist.pop(itemdeleted)
            except:
                print("Incorrect selection.")
                t=True
        elif(choice==3):
            print("The following items remain in the list:")
            for i in mylist :
                print(i)
                t=False
        else:
            print("Incorrect selection.")
            t=True

    

                
    
