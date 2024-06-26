print("Words in an alphabetical order:")
with open('word.txt','r') as files:
    content=files.readlines()
    content.sort()
    for i in content:
        print(i)
    
    

    
    
        
