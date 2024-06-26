import random

t=True
while t:
    option=('nuke','foot','cockroach')
    mychoice=input("Foot, Nuke or Cockroach? (Quit ends): ")
    print("you choice: ",mychoice)
    computerchoice=random.randint(1,3)
    if(computerchoice==1):
        choice=='Foot'
    elif(computerchoice==2):
        choice='Nuke'
    elif(computerchoice==3):
        choice:'Cockroach'

    print("Computer choice:",choice)
