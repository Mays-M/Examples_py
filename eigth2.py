import sys
def insertfile():
    filename=input("Give the file name: ")
    return filename
 
        


def main():
    f=insertfile()
    try:
        content=open(f,'r')
        filecontent=content.read()
        re=int(filecontent)
        result=(1000/re)
    except IOError:
        print("There seems to be no file with that name.")
    except(TypeError,ValueError):
        print("The file contents were unsuitable.")
    else:
        print("The result was ",+result)
            

if __name__=="__main__":
    main()
