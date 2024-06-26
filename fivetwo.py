import os
name=""
name=input("write file")
something=input("Write something: ")
with open(name,'r+')as f:
	  content=f.write()
	  f2=f.read()
	  print("Wrote ",something,"  to the file ",name)
	  print(f2)
        
          
