
import time
t=True
while t:
	with open("notebook.txt","a") as content:
		print("(1) Read the notebook")
		print("(2) Add note")
		print("(3) Empty the notebook")
		print("(4) Quit")
		select=input("Please select one: ")
		if(select=='1'):
			 with open("notebook.txt","r") as f:
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
	  
