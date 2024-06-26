class player:
    def __init__(self,teamcolor):
        self.teamcolor=teamcolor
        self.__point=0
    def tellscore(self):
        return self.teamcolor
            
    def setgoal(self,point):
        self.__point=point
    def getgoal(self):
        return self.__point

def main():
    p=player("Blue")
    
    print("I am ",p.tellscore() ," we have",(p.getgoal())+1, "pints!")


if __name__=="__main__":
    main()

            

    
