class player:
    teamcolor="Blue"
    __points=0
    def __init__(self):
        self.teamcolor=input("What color do I get?:" )
    def tellscore(self):
        print("I am ",self.teamcolor+" we have ",self.__points,"points")
    def goal(self):
        self.__points +=1
    def printout(self):
        print("I am ",self.teamcolor," we have ",self.__points,"points")
		
def main():
    p1=player()
    p2=player()
    p1.goal()
    p1.goal()
    p2.goal()
    p1.tellscore()
    p2.tellscore()
                
		
	
	
if __name__=="__main__":
	main()
