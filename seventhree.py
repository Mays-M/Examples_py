import random
i=0
t=True
youwin,computerwin,bothlosing=0,0,0
win={('Nuke','Foot'):True,('Nuke','Cockroach'):True,('Foot','Cockroach'):True,('Cockroach','Nuke'):True }
bothlose={('Nuke','Nuke'):True,('Cockroach','Cockroach'):True,('Foot','Foot'):True}
def checkwin(choice1,choice2):
        result=win.get((choice1,choice2),False)
        return result
def checkbothlose(choice1,choice2):
	result=bothlose.get((choice1,choice2),False)
	return result
while t:
        computerchoice=random.randint(1,3)
        if(computerchoice==1):
                computerchoice='Foot'
        elif(computerchoice==2):
                computerchoice='Nuke'
        else:
                computerchoice='Cockroach'
        while t:
                mychoice=input("Foot, Nuke or Cockroach? (Quit ends): ")
        
                if ((mychoice !='Quit') and ((mychoice=='Foot') or (mychoice=='Nuke') or (mychoice=='Cockroach'))):
                        print("you chose: ",mychoice)
                        print('Computer chose:',computerchoice)
                        result=checkwin(mychoice,computerchoice)
                        result2=checkbothlose(mychoice,computerchoice)
                        if result:
                                print('You WIN!')
                                youwin +=1
                                i+=1
                        elif result2:
                                print('It is a tie!')
                                
                                bothlosing +=1
                                i +=1
                        else:
                                print('You LOSE!')
                                computerwin +=1
                                i +=1

                elif(mychoice=='Quit'):
                        
                        t=False
                else:
                        print('Incorrect selection.')
                        break
else:
        print("You played",+ i,"rounds, and won",+ youwin ,'rounds', ',playing tie in',+ bothlosing ,'rounds.')
