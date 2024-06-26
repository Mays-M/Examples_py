import inspector

while True:
    userinput = input("Give a string for testing: ")
    tulos = inspector.testme(userinput)
    if tulos == True:
        print("This string fits for a password!")
        break
    else:
        print("The module says no.")
