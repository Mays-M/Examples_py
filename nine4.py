import pickle
import time    
def main():
    t=True
    note=[]
    filename="notebooks.dat"
    try:
        with open('noteboobk.dat','rb')as content:
            pickle.load(content)
    except IOError:
            print("No default notebook was found, created one.")
            with open('notebook.dat','bw')as contentwrite:
                pickle.dump(note,contentwrite)
    while t:
            print("(1) Read the notebook")
            print("(2) Add note")
            print("(3) Edit a note")
            print("(4) Delete a note")
            print("(5) Save and quit")
            userselection=input("Please select one: ")
            if(userselection=='1'):
                for i in note:
                    print(i)
            elif(userselection=='2'):
                noteitem=input("Write a new note: ")
                noteitem=noteitem + ':::'
                noteitem +=time.strftime('%x %x')
                note.append(noteitem)
            elif(userselection=='3'):
                print("The list has",len(note),"notes.")
                try:
                    whichitem=int(input("Which of them will be changed?: "))
                    print(note[whichitem])
                    newnote=input("Give the new note: ")
                    newnote =newnote+':::'
                    newnote +=time.strftime('%x %x')
                    note.pop(whichitem)
                    note.insert(whichitem,newnote + '\n')
                except Exception:
                    print("Incorrect selection.")
            elif(userselection=='4'):
                try:
                    print("The list has",len(note),"notes.")
                    itemdelete=int(input("Which of them will be deleted?: "))
                    print("Deleted note",note[itemdelete])
                    note.pop(itemdelete)
                except Exception:
                    print("Deleted note",note[0])
                    note.pop(0)
            elif(userselection=='5'):
                try:
                    writefile=open(filename,'wb')
                    content=pickle.dump(note,writefile)
                    writefile.close()
                except IOError:
                    return False
                print("Notebook shutting down, thank you.")
                break
            else:
                t=True

if __name__=="__main__":
    main()
            
        
            
            

    


    
    
    
    
    

    
        
